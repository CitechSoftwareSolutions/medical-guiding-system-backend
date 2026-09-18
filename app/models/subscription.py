from datetime import datetime
from typing import Optional, List, TYPE_CHECKING
from sqlalchemy import String, Integer, Text, Numeric, ForeignKey, DateTime, func, JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.database import Base

if TYPE_CHECKING:
    from app.models.doctor import DoctorProfile
    from app.models.student import StudentProfile
    from app.models.payment import Payment


class Plan(Base):
    __tablename__ = "plans"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    doctor_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("doctor_profiles.id", ondelete="SET NULL"), nullable=True, index=True
    )
    name: Mapped[str] = mapped_column(String(100), nullable=False, index=True)
    price: Mapped[float] = mapped_column(Numeric(10, 2), default=0.00, server_default="0.00", nullable=False)
    duration_days: Mapped[int] = mapped_column(Integer, default=30, server_default="30", nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    features: Mapped[Optional[list]] = mapped_column(JSON, nullable=True)
    status: Mapped[str] = mapped_column(
        String(20), default="active", server_default="active", nullable=False
    )  # 'active', 'inactive', 'archived'
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False
    )

    # Relationships
    doctor: Mapped[Optional["DoctorProfile"]] = relationship("DoctorProfile", back_populates="plans")
    subscriptions: Mapped[List["StudentSubscription"]] = relationship(
        "StudentSubscription", back_populates="plan", cascade="all, delete-orphan"
    )
    payments: Mapped[List["Payment"]] = relationship("Payment", back_populates="plan")

    def __repr__(self) -> str:
        return f"<Plan(id={self.id}, name='{self.name}', price={self.price})>"


class StudentSubscription(Base):
    __tablename__ = "student_subscriptions"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    student_id: Mapped[int] = mapped_column(
        ForeignKey("student_profiles.id", ondelete="CASCADE"), nullable=False, index=True
    )
    plan_id: Mapped[int] = mapped_column(
        ForeignKey("plans.id", ondelete="RESTRICT"), nullable=False, index=True
    )
    payment_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("payments.id", ondelete="SET NULL"), nullable=True, unique=True, index=True
    )
    status: Mapped[str] = mapped_column(
        String(20), default="active", server_default="active", nullable=False
    )  # 'pending', 'active', 'expired', 'cancelled', 'failed'
    start_date: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    end_date: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False
    )

    # Relationships
    student: Mapped["StudentProfile"] = relationship("StudentProfile", back_populates="subscriptions")
    plan: Mapped["Plan"] = relationship("Plan", back_populates="subscriptions")
    payment: Mapped[Optional["Payment"]] = relationship("Payment", back_populates="subscription")

    def __repr__(self) -> str:
        return f"<StudentSubscription(id={self.id}, student_id={self.student_id}, plan_id={self.plan_id}, status='{self.status}')>"
