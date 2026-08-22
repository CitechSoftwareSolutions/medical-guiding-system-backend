from typing import Annotated, List, Optional
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.deps import get_db, get_current_user
from app.models.user import User
from app.schemas.subscription import SubscriptionCreate, SubscriptionRead
from app.services.subscription_service import SubscriptionService
from app.services.student_service import StudentService
from app.services.audit_service import AuditService

router = APIRouter(prefix="/subscriptions", tags=["Student Subscriptions"])


@router.post("/subscribe", response_model=SubscriptionRead, status_code=status.HTTP_201_CREATED)
def subscribe_to_plan(
    sub_in: SubscriptionCreate,
    current_user: Annotated[User, Depends(get_current_user)],
    db: Annotated[Session, Depends(get_db)],
):
    student_profile = StudentService.get_by_user_id(db=db, user_id=current_user.id)
    if not student_profile:
        raise HTTPException(status_code=400, detail="Only student accounts can subscribe to plans")

    subscription = SubscriptionService.subscribe_student(
        db=db,
        student_id=student_profile.id,
        plan_id=sub_in.plan_id,
        payment_id=sub_in.payment_id,
    )
    AuditService.log(
        db=db,
        user_id=current_user.id,
        action="SUBSCRIBE_PLAN",
        entity="StudentSubscription",
        entity_id=str(subscription.id),
    )
    return subscription


@router.get("/my-subscription", response_model=Optional[SubscriptionRead])
def get_my_active_subscription(
    current_user: Annotated[User, Depends(get_current_user)],
    db: Annotated[Session, Depends(get_db)],
):
    student_profile = StudentService.get_by_user_id(db=db, user_id=current_user.id)
    if not student_profile:
        raise HTTPException(status_code=400, detail="Current user is not a student")
    return SubscriptionService.get_student_active_subscription(db=db, student_id=student_profile.id)


@router.get("/history", response_model=List[SubscriptionRead])
def get_my_subscription_history(
    current_user: Annotated[User, Depends(get_current_user)],
    db: Annotated[Session, Depends(get_db)],
):
    student_profile = StudentService.get_by_user_id(db=db, user_id=current_user.id)
    if not student_profile:
        raise HTTPException(status_code=400, detail="Current user is not a student")
    return SubscriptionService.list_student_subscriptions(db=db, student_id=student_profile.id)
