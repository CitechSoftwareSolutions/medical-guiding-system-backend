from typing import Annotated, List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.deps import get_db, get_current_user, require_role
from app.models.user import User
from app.schemas.student import StudentProfileRead, StudentProfileUpdate
from app.services.student_service import StudentService

router = APIRouter(prefix="/students", tags=["Students"])


@router.get("/", response_model=List[StudentProfileRead], dependencies=[Depends(require_role("Admin", "Doctor", "Owner"))])
def list_students(
    db: Annotated[Session, Depends(get_db)],
    skip: int = 0,
    limit: int = 50,
):
    return StudentService.list_students(db=db, skip=skip, limit=limit)


@router.get("/me/profile", response_model=StudentProfileRead)
def get_my_student_profile(
    current_user: Annotated[User, Depends(get_current_user)],
    db: Annotated[Session, Depends(get_db)],
):
    profile = StudentService.get_by_user_id(db=db, user_id=current_user.id)
    if not profile:
        raise HTTPException(status_code=404, detail="Student profile not found for current user")
    return profile


@router.get("/{student_id}", response_model=StudentProfileRead)
def get_student(
    student_id: int,
    db: Annotated[Session, Depends(get_db)],
    current_user: Annotated[User, Depends(get_current_user)],
):
    student = StudentService.get_by_id(db=db, student_id=student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    user_roles = [ur.role.name for ur in current_user.user_roles if ur.role]
    if student.user_id != current_user.id and not any(r in user_roles for r in ["Admin", "Doctor", "Owner"]):
        raise HTTPException(status_code=403, detail="Not authorized to view this profile")

    return student


@router.put("/{student_id}", response_model=StudentProfileRead)
def update_student_profile(
    student_id: int,
    profile_in: StudentProfileUpdate,
    current_user: Annotated[User, Depends(get_current_user)],
    db: Annotated[Session, Depends(get_db)],
):
    student = StudentService.get_by_id(db=db, student_id=student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    user_roles = [ur.role.name for ur in current_user.user_roles if ur.role]
    if student.user_id != current_user.id and "Admin" not in user_roles and "Owner" not in user_roles:
        raise HTTPException(status_code=403, detail="Not authorized to modify this profile")

    return StudentService.update_profile(db=db, student_id=student_id, profile_in=profile_in)
