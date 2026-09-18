import uuid
from typing import List, Optional
from sqlalchemy import select
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.models.payment import Payment
from app.schemas.payment import PaymentCreate, PaymentUpdate
from app.services.subscription_service import SubscriptionService


class PaymentService:
    @staticmethod
    def create_payment(
        db: Session, student_id: int, payment_in: PaymentCreate
    ) -> Payment:
        tx_id = payment_in.transaction_id or f"TXN-{uuid.uuid4().hex[:12].upper()}"
        payment = Payment(
            student_id=student_id,
            plan_id=payment_in.plan_id,
            amount=payment_in.amount,
            currency=payment_in.currency or "USD",
            gateway=payment_in.gateway or "manual",
            transaction_id=tx_id,
            status="successful",  # for current dev / manual workflow
        )
        db.add(payment)
        db.commit()
        db.refresh(payment)

        # If payment is for a plan and successful, automatically activate subscription
        if payment.plan_id and payment.status == "successful":
            SubscriptionService.subscribe_student(
                db=db,
                student_id=student_id,
                plan_id=payment.plan_id,
                payment_id=payment.id,
            )

        return payment

    @staticmethod
    def list_payments(
        db: Session, student_id: Optional[int] = None, skip: int = 0, limit: int = 50
    ) -> List[Payment]:
        stmt = select(Payment)
        if student_id:
            stmt = stmt.where(Payment.student_id == student_id)
        return list(db.scalars(stmt.order_by(Payment.created_at.desc()).offset(skip).limit(limit)).all())
