from typing import List, Optional
from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload
from fastapi import HTTPException, status

from app.models.student import StudentProfile
from app.schemas.student import StudentProfileCreate, StudentProfileUpdate


class StudentService:
    @staticmethod
    def get_by_id(db: Session, student_id: int) -> Optional[StudentProfile]:
        return db.scalar(
            select(StudentProfile)
            .where(StudentProfile.id == student_id)
            .options(selectinload(StudentProfile.user))
        )

    @staticmethod
    def get_by_user_id(db: Session, user_id: int) -> Optional[StudentProfile]:
        return db.scalar(
            select(StudentProfile)
            .where(StudentProfile.user_id == user_id)
            .options(selectinload(StudentProfile.user))
        )

    @staticmethod
    def list_students(db: Session, skip: int = 0, limit: int = 50) -> List[StudentProfile]:
        return list(
            db.scalars(
                select(StudentProfile)
                .options(selectinload(StudentProfile.user))
                .offset(skip)
                .limit(limit)
            ).all()
        )

    @staticmethod
    def update_profile(
        db: Session, student_id: int, profile_in: StudentProfileUpdate
    ) -> StudentProfile:
        student = db.get(StudentProfile, student_id)
        if not student:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student profile not found")

        update_data = profile_in.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(student, key, value)

        db.commit()
        db.refresh(student)
        return student
