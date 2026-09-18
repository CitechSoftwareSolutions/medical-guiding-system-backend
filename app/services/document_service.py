from datetime import datetime
from typing import List, Optional
from sqlalchemy import select, or_
from sqlalchemy.orm import Session, selectinload
from fastapi import HTTPException, status

from app.models.document import Category, Document, StudentDocument
from app.models.student import StudentProfile
from app.models.subscription import StudentSubscription
from app.schemas.category import CategoryCreate, CategoryUpdate
from app.schemas.document import DocumentCreate, DocumentUpdate, StudentDocumentGrant


class DocumentService:
    # Categories
    @staticmethod
    def create_category(db: Session, cat_in: CategoryCreate) -> Category:
        existing = db.scalar(select(Category).where(Category.name == cat_in.name))
        if existing:
            raise HTTPException(status_code=400, detail="Category name already exists")
        cat = Category(name=cat_in.name, description=cat_in.description)
        db.add(cat)
        db.commit()
        db.refresh(cat)
        return cat

    @staticmethod
    def list_categories(db: Session) -> List[Category]:
        return list(db.scalars(select(Category).order_by(Category.name)).all())

    # Documents
    @staticmethod
    def create_document(db: Session, doc_in: DocumentCreate, doctor_id: int) -> Document:
        doc = Document(
            doctor_id=doctor_id,
            category_id=doc_in.category_id,
            title=doc_in.title,
            description=doc_in.description,
            file_url=doc_in.file_url,
            visibility=doc_in.visibility or "free",
        )
        db.add(doc)
        db.commit()
        db.refresh(doc)
        return doc

    @staticmethod
    def get_document(db: Session, doc_id: int) -> Optional[Document]:
        return db.scalar(
            select(Document)
            .where(Document.id == doc_id)
            .options(selectinload(Document.category), selectinload(Document.doctor))
        )

    @staticmethod
    def list_documents(
        db: Session,
        category_id: Optional[int] = None,
        visibility: Optional[str] = None,
        skip: int = 0,
        limit: int = 50,
    ) -> List[Document]:
        stmt = select(Document).options(selectinload(Document.category))
        if category_id:
            stmt = stmt.where(Document.category_id == category_id)
        if visibility:
            stmt = stmt.where(Document.visibility == visibility)
        stmt = stmt.order_by(Document.created_at.desc()).offset(skip).limit(limit)
        return list(db.scalars(stmt).all())

    @staticmethod
    def update_document(db: Session, doc_id: int, doc_in: DocumentUpdate) -> Document:
        doc = db.get(Document, doc_id)
        if not doc:
            raise HTTPException(status_code=404, detail="Document not found")
        for key, value in doc_in.model_dump(exclude_unset=True).items():
            setattr(doc, key, value)
        db.commit()
        db.refresh(doc)
        return doc

    @staticmethod
    def delete_document(db: Session, doc_id: int) -> None:
        doc = db.get(Document, doc_id)
        if not doc:
            raise HTTPException(status_code=404, detail="Document not found")
        db.delete(doc)
        db.commit()

    # Access Control
    @staticmethod
    def grant_access(db: Session, grant_in: StudentDocumentGrant) -> StudentDocument:
        student = db.get(StudentProfile, grant_in.student_id)
        if not student:
            raise HTTPException(status_code=404, detail="Student not found")
        doc = db.get(Document, grant_in.document_id)
        if not doc:
            raise HTTPException(status_code=404, detail="Document not found")

        existing = db.scalar(
            select(StudentDocument).where(
                StudentDocument.student_id == grant_in.student_id,
                StudentDocument.document_id == grant_in.document_id,
            )
        )
        if existing:
            existing.access_type = grant_in.access_type or "granted"
            existing.expires_at = grant_in.expires_at
            db.commit()
            db.refresh(existing)
            return existing

        access = StudentDocument(
            student_id=grant_in.student_id,
            document_id=grant_in.document_id,
            access_type=grant_in.access_type or "granted",
            expires_at=grant_in.expires_at,
        )
        db.add(access)
        db.commit()
        db.refresh(access)
        return access

    @staticmethod
    def check_student_has_access(db: Session, student_id: int, document_id: int) -> bool:
        doc = db.get(Document, document_id)
        if not doc:
            return False
        if doc.visibility == "free":
            return True

        # Check direct grant
        now = datetime.now()
        grant = db.scalar(
            select(StudentDocument).where(
                StudentDocument.student_id == student_id,
                StudentDocument.document_id == document_id,
                or_(StudentDocument.expires_at.is_(None), StudentDocument.expires_at > now),
            )
        )
        if grant:
            return True

        # Check active subscription
        sub = db.scalar(
            select(StudentSubscription).where(
                StudentSubscription.student_id == student_id,
                StudentSubscription.status == "active",
                StudentSubscription.end_date > now,
            )
        )
        if sub:
            return True

        return False

    @staticmethod
    def get_student_documents(db: Session, student_id: int) -> List[StudentDocument]:
        return list(
            db.scalars(
                select(StudentDocument)
                .where(StudentDocument.student_id == student_id)
                .options(
                    selectinload(StudentDocument.document).selectinload(Document.category)
                )
            ).all()
        )
