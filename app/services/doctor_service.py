from typing import List, Optional
from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload
from fastapi import HTTPException, status

from app.models.doctor import DoctorProfile
from app.schemas.doctor import DoctorProfileCreate, DoctorProfileUpdate


class DoctorService:
    @staticmethod
    def get_by_id(db: Session, doctor_id: int) -> Optional[DoctorProfile]:
        return db.scalar(
            select(DoctorProfile)
            .where(DoctorProfile.id == doctor_id)
            .options(selectinload(DoctorProfile.user))
        )

    @staticmethod
    def get_by_user_id(db: Session, user_id: int) -> Optional[DoctorProfile]:
        return db.scalar(
            select(DoctorProfile)
            .where(DoctorProfile.user_id == user_id)
            .options(selectinload(DoctorProfile.user))
        )

    @staticmethod
    def list_doctors(db: Session, skip: int = 0, limit: int = 50) -> List[DoctorProfile]:
        return list(
            db.scalars(
                select(DoctorProfile)
                .options(selectinload(DoctorProfile.user))
                .offset(skip)
                .limit(limit)
            ).all()
        )

    @staticmethod
    def update_profile(
        db: Session, doctor_id: int, profile_in: DoctorProfileUpdate
    ) -> DoctorProfile:
        doctor = db.get(DoctorProfile, doctor_id)
        if not doctor:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Doctor profile not found")

        update_data = profile_in.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(doctor, key, value)

        db.commit()
        db.refresh(doctor)
        return doctor
