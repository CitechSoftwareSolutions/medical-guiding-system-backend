from datetime import datetime
from typing import Optional, List, TYPE_CHECKING
from sqlalchemy import String, ForeignKey, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.database import Base

if TYPE_CHECKING:
    from app.models.user import User
    from app.models.document import StudentDocument
    from app.models.subscription import StudentSubscription
    from app.models.payment import Payment
    from app.models.chat import ChatSession


class StudentProfile(Base):
    __tablename__ = "student_profiles"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"), unique=True, nullable=False, index=True
    )
    university: Mapped[Optional[str]] = mapped_column(String(200), nullable=True)
    batch: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    year: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    country: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False
    )

    # Relationships
    user: Mapped["User"] = relationship("User", back_populates="student_profile")
    student_documents: Mapped[List["StudentDocument"]] = relationship(
        "StudentDocument", back_populates="student", cascade="all, delete-orphan"
    )
    subscriptions: Mapped[List["StudentSubscription"]] = relationship(
        "StudentSubscription", back_populates="student", cascade="all, delete-orphan"
    )
    payments: Mapped[List["Payment"]] = relationship(
        "Payment", back_populates="student", cascade="all, delete-orphan"
    )
    chat_sessions: Mapped[List["ChatSession"]] = relationship(
        "ChatSession", back_populates="student", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"<StudentProfile(id={self.id}, user_id={self.user_id}, university='{self.university}')>"
