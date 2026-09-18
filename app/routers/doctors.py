from typing import Annotated, List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.deps import get_db, get_current_user, require_role
from app.models.user import User
from app.schemas.doctor import DoctorProfileRead, DoctorProfileUpdate
from app.services.doctor_service import DoctorService

router = APIRouter(prefix="/doctors", tags=["Doctors"])


@router.get("/", response_model=List[DoctorProfileRead])
def list_doctors(
    db: Annotated[Session, Depends(get_db)],
    skip: int = 0,
    limit: int = 50,
):
    return DoctorService.list_doctors(db=db, skip=skip, limit=limit)


@router.get("/me/profile", response_model=DoctorProfileRead)
def get_my_doctor_profile(
    current_user: Annotated[User, Depends(get_current_user)],
    db: Annotated[Session, Depends(get_db)],
):
    profile = DoctorService.get_by_user_id(db=db, user_id=current_user.id)
    if not profile:
        raise HTTPException(status_code=404, detail="Doctor profile not found for current user")
    return profile


@router.get("/{doctor_id}", response_model=DoctorProfileRead)
def get_doctor(
    doctor_id: int,
    db: Annotated[Session, Depends(get_db)],
):
    doctor = DoctorService.get_by_id(db=db, doctor_id=doctor_id)
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return doctor


@router.put("/{doctor_id}", response_model=DoctorProfileRead)
def update_doctor_profile(
    doctor_id: int,
    profile_in: DoctorProfileUpdate,
    current_user: Annotated[User, Depends(get_current_user)],
    db: Annotated[Session, Depends(get_db)],
):
    doctor = DoctorService.get_by_id(db=db, doctor_id=doctor_id)
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")

    user_roles = [ur.role.name for ur in current_user.user_roles if ur.role]
    if doctor.user_id != current_user.id and "Admin" not in user_roles and "Owner" not in user_roles:
        raise HTTPException(status_code=403, detail="Not authorized to modify this profile")

    return DoctorService.update_profile(db=db, doctor_id=doctor_id, profile_in=profile_in)
