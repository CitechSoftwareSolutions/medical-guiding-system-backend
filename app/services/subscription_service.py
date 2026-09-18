from datetime import datetime, timedelta, timezone
from typing import List, Optional
from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload
from fastapi import HTTPException, status

from app.models.subscription import Plan, StudentSubscription
from app.schemas.plan import PlanCreate, PlanUpdate
from app.schemas.subscription import SubscriptionCreate, SubscriptionUpdate


class SubscriptionService:
    # Plans
    @staticmethod
    def create_plan(db: Session, plan_in: PlanCreate, doctor_id: Optional[int] = None) -> Plan:
        plan = Plan(
            doctor_id=doctor_id or plan_in.doctor_id,
            name=plan_in.name,
            price=plan_in.price,
            duration_days=plan_in.duration_days,
            description=plan_in.description,
            status="active",
        )
        db.add(plan)
        db.commit()
        db.refresh(plan)
        return plan

    @staticmethod
    def list_plans(db: Session, active_only: bool = True) -> List[Plan]:
        stmt = select(Plan)
        if active_only:
            stmt = stmt.where(Plan.status == "active")
        return list(db.scalars(stmt.order_by(Plan.price.asc())).all())

    @staticmethod
    def get_plan(db: Session, plan_id: int) -> Optional[Plan]:
        return db.get(Plan, plan_id)

    @staticmethod
    def update_plan(db: Session, plan_id: int, plan_in: PlanUpdate) -> Plan:
        plan = db.get(Plan, plan_id)
        if not plan:
            raise HTTPException(status_code=404, detail="Plan not found")
        for key, value in plan_in.model_dump(exclude_unset=True).items():
            setattr(plan, key, value)
        db.commit()
        db.refresh(plan)
        return plan

    # Subscriptions
    @staticmethod
    def subscribe_student(
        db: Session, student_id: int, plan_id: int, payment_id: Optional[int] = None
    ) -> StudentSubscription:
        plan = db.get(Plan, plan_id)
        if not plan or plan.status != "active":
            raise HTTPException(status_code=400, detail="Selected plan is not available")

        now = datetime.now(timezone.utc)
        end_date = now + timedelta(days=plan.duration_days)

        # Deactivate any currently active subscriptions for this student
        active_subs = db.scalars(
            select(StudentSubscription).where(
                StudentSubscription.student_id == student_id,
                StudentSubscription.status == "active",
            )
        ).all()
        for sub in active_subs:
            sub.status = "expired"

        new_sub = StudentSubscription(
            student_id=student_id,
            plan_id=plan_id,
            payment_id=payment_id,
            status="active",
            start_date=now,
            end_date=end_date,
        )
        db.add(new_sub)
        db.commit()
        db.refresh(new_sub)
        return new_sub

    @staticmethod
    def get_student_active_subscription(
        db: Session, student_id: int
    ) -> Optional[StudentSubscription]:
        now = datetime.now(timezone.utc)
        return db.scalar(
            select(StudentSubscription)
            .where(
                StudentSubscription.student_id == student_id,
                StudentSubscription.status == "active",
                StudentSubscription.end_date > now,
            )
            .options(selectinload(StudentSubscription.plan))
        )

    @staticmethod
    def list_student_subscriptions(
        db: Session, student_id: int
    ) -> List[StudentSubscription]:
        return list(
            db.scalars(
                select(StudentSubscription)
                .where(StudentSubscription.student_id == student_id)
                .options(selectinload(StudentSubscription.plan))
                .order_by(StudentSubscription.created_at.desc())
            ).all()
        )
