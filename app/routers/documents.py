import os
import shutil
from typing import Annotated, List, Optional
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form, status
from sqlalchemy.orm import Session

from app.core.config import settings
from app.core.deps import get_db, get_current_user, get_optional_current_user, require_role
from app.models.user import User
from app.schemas.document import (
    DocumentCreate,
    DocumentUpdate,
    DocumentRead,
    StudentDocumentGrant,
    StudentDocumentRead,
)
from app.services.document_service import DocumentService
from app.services.doctor_service import DoctorService
from app.services.student_service import StudentService
from app.services.audit_service import AuditService

router = APIRouter(prefix="/documents", tags=["Documents"])


@router.get("/", response_model=List[DocumentRead])
def list_documents(
    db: Annotated[Session, Depends(get_db)],
    category_id: Optional[int] = None,
    visibility: Optional[str] = None,
    skip: int = 0,
    limit: int = 50,
):
    return DocumentService.list_documents(
        db=db, category_id=category_id, visibility=visibility, skip=skip, limit=limit
    )


@router.get("/{document_id}", response_model=DocumentRead)
def get_document(
    document_id: int,
    db: Annotated[Session, Depends(get_db)],
    current_user: Annotated[Optional[User], Depends(get_optional_current_user)],
):
    doc = DocumentService.get_document(db=db, doc_id=document_id)
    if not doc:
        raise HTTPException(status_code=404, detail="Document not found")

    if doc.visibility == "free":
        return doc

    # If document is premium or restricted, verify access
    if not current_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authentication required to view this document",
        )

    user_roles = [ur.role.name for ur in current_user.user_roles if ur.role]
    if "Admin" in user_roles or "Owner" in user_roles:
        return doc

    if "Doctor" in user_roles:
        doctor_profile = DoctorService.get_by_user_id(db=db, user_id=current_user.id)
        if doctor_profile and doc.doctor_id == doctor_profile.id:
            return doc

    student_profile = StudentService.get_by_user_id(db=db, user_id=current_user.id)
    if student_profile:
        has_access = DocumentService.check_student_has_access(
            db=db, student_id=student_profile.id, document_id=document_id
        )
        if has_access:
            return doc

    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Subscription or granted access required to view this document",
    )


@router.post("/", response_model=DocumentRead, status_code=status.HTTP_201_CREATED)
def create_document(
    doc_in: DocumentCreate,
    current_user: Annotated[User, Depends(require_role("Doctor", "Admin", "Owner"))],
    db: Annotated[Session, Depends(get_db)],
):
    doctor_profile = DoctorService.get_by_user_id(db=db, user_id=current_user.id)
    if not doctor_profile:
        # Fallback if admin creating on behalf or create doctor profile
        doctor_profile = DoctorService.list_doctors(db=db, limit=1)
        if not doctor_profile:
            raise HTTPException(status_code=400, detail="No doctor profile available to attach document")
        doctor_id = doctor_profile[0].id
    else:
        doctor_id = doctor_profile.id

    doc = DocumentService.create_document(db=db, doc_in=doc_in, doctor_id=doctor_id)
    AuditService.log(
        db=db,
        user_id=current_user.id,
        action="UPLOAD_DOCUMENT",
        entity="Document",
        entity_id=str(doc.id),
    )
    return doc


@router.post("/upload", response_model=dict)
def upload_file(
    file: UploadFile = File(...),
    current_user: Annotated[User, Depends(require_role("Doctor", "Admin", "Owner"))] = None,
):
    os.makedirs(settings.UPLOAD_DIR, exist_ok=True)
    file_name = f"{current_user.id}_{file.filename}"
    file_path = os.path.join(settings.UPLOAD_DIR, file_name)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    file_url = f"/uploads/{file_name}"
    return {"file_url": file_url, "filename": file.filename}


@router.put("/{document_id}", response_model=DocumentRead)
def update_document(
    document_id: int,
    doc_in: DocumentUpdate,
    current_user: Annotated[User, Depends(require_role("Doctor", "Admin", "Owner"))],
    db: Annotated[Session, Depends(get_db)],
):
    return DocumentService.update_document(db=db, doc_id=document_id, doc_in=doc_in)


@router.delete("/{document_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_document(
    document_id: int,
    current_user: Annotated[User, Depends(require_role("Doctor", "Admin", "Owner"))],
    db: Annotated[Session, Depends(get_db)],
):
    DocumentService.delete_document(db=db, doc_id=document_id)
    AuditService.log(
        db=db,
        user_id=current_user.id,
        action="DELETE_DOCUMENT",
        entity="Document",
        entity_id=str(document_id),
    )


@router.post("/grant-access", response_model=StudentDocumentRead)
def grant_access(
    grant_in: StudentDocumentGrant,
    current_user: Annotated[User, Depends(require_role("Doctor", "Admin", "Owner"))],
    db: Annotated[Session, Depends(get_db)],
):
    return DocumentService.grant_access(db=db, grant_in=grant_in)


@router.get("/student/my-documents", response_model=List[StudentDocumentRead])
def get_my_documents(
    current_user: Annotated[User, Depends(get_current_user)],
    db: Annotated[Session, Depends(get_db)],
):
    student_profile = StudentService.get_by_user_id(db=db, user_id=current_user.id)
    if not student_profile:
        raise HTTPException(status_code=400, detail="Current user is not registered as a student")
    return DocumentService.get_student_documents(db=db, student_id=student_profile.id)
