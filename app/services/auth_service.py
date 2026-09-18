from typing import Optional, List
from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload
from fastapi import HTTPException, status

from app.core.security import hash_password, verify_password
from app.models.user import User
from app.models.role import Role, UserRole
from app.models.doctor import DoctorProfile
from app.models.student import StudentProfile
from app.schemas.auth import UserRegister


class AuthService:
    @staticmethod
    def register_user(db: Session, user_in: UserRegister) -> User:
        # Check if email exists
        existing = db.scalar(select(User).where(User.email == user_in.email.lower()))
        if existing:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="A user with this email already exists."
            )

        new_user = User(
            email=user_in.email.lower(),
            password_hash=hash_password(user_in.password),
            first_name=user_in.first_name,
            last_name=user_in.last_name,
            phone=user_in.phone,
            status="active",
            email_verified=False
        )
        db.add(new_user)
        db.flush()  # assign user.id

        # Assign Role (Student or Doctor)
        role_name = (user_in.role or "Student").capitalize()
        role = db.scalar(select(Role).where(Role.name == role_name))
        if not role:
            # Create role if missing
            role = Role(name=role_name, description=f"{role_name} role")
            db.add(role)
            db.flush()

        user_role = UserRole(user_id=new_user.id, role_id=role.id)
        db.add(user_role)

        # Create corresponding profile
        if role_name == "Doctor":
            doctor_profile = DoctorProfile(user_id=new_user.id)
            db.add(doctor_profile)
        else:
            student_profile = StudentProfile(user_id=new_user.id)
            db.add(student_profile)

        db.commit()
        db.refresh(new_user)
        return new_user

    @staticmethod
    def authenticate_user(db: Session, email: str, password: str) -> Optional[User]:
        stmt = (
            select(User)
            .where(User.email == email.lower())
            .options(
                selectinload(User.user_roles).selectinload(UserRole.role),
                selectinload(User.doctor_profile),
                selectinload(User.student_profile),
            )
        )
        user = db.scalar(stmt)
        if not user:
            return None
        if not verify_password(password, user.password_hash):
            return None
        return user

    @staticmethod
    def assign_role(db: Session, user_id: int, role_id: int) -> UserRole:
        user = db.get(User, user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        role = db.get(Role, role_id)
        if not role:
            raise HTTPException(status_code=404, detail="Role not found")

        existing = db.scalar(
            select(UserRole).where(UserRole.user_id == user_id, UserRole.role_id == role_id)
        )
        if existing:
            return existing

        user_role = UserRole(user_id=user_id, role_id=role_id)
        db.add(user_role)
        db.commit()
        db.refresh(user_role)
        return user_role

    @staticmethod
    def change_password(db: Session, user_id: int, old_pass: str, new_pass: str) -> None:
        user = db.get(User, user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        if not verify_password(old_pass, user.password_hash):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Incorrect current password",
            )
        user.password_hash = hash_password(new_pass)
        db.commit()
