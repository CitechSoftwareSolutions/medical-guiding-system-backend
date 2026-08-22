from datetime import datetime
from typing import Optional, TYPE_CHECKING
from sqlalchemy import String, Integer, Numeric, ForeignKey, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.database import Base

if TYPE_CHECKING:
    from app.models.student import StudentProfile
    from app.models.subscription import Plan, StudentSubscription


class Payment(Base):
    __tablename__ = "payments"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    student_id: Mapped[int] = mapped_column(
        ForeignKey("student_profiles.id", ondelete="CASCADE"), nullable=False, index=True
    )
    plan_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("plans.id", ondelete="SET NULL"), nullable=True, index=True
    )
    amount: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)
    currency: Mapped[str] = mapped_column(String(10), default="USD", server_default="USD", nullable=False)
    gateway: Mapped[str] = mapped_column(String(50), default="manual", server_default="manual", nullable=False)
    transaction_id: Mapped[Optional[str]] = mapped_column(String(100), unique=True, nullable=True, index=True)
    status: Mapped[str] = mapped_column(
        String(20), default="pending", server_default="pending", nullable=False
    )  # 'pending', 'successful', 'failed', 'refunded'
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    # Relationships
    student: Mapped["StudentProfile"] = relationship("StudentProfile", back_populates="payments")
    plan: Mapped[Optional["Plan"]] = relationship("Plan", back_populates="payments")
    subscription: Mapped[Optional["StudentSubscription"]] = relationship(
        "StudentSubscription", back_populates="payment", uselist=False
    )

    def __repr__(self) -> str:
        return f"<Payment(id={self.id}, student_id={self.student_id}, amount={self.amount}, status='{self.status}')>"
