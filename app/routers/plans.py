from typing import Annotated, List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.core.deps import get_db, require_role, get_current_user
from app.models.user import User
from app.schemas.plan import PlanCreate, PlanUpdate, PlanRead
from app.services.subscription_service import SubscriptionService
from app.services.doctor_service import DoctorService
from app.services.audit_service import AuditService

router = APIRouter(prefix="/plans", tags=["Subscription Plans"])


@router.get("/", response_model=List[PlanRead])
def list_plans(
    db: Annotated[Session, Depends(get_db)],
    active_only: bool = True,
):
    return SubscriptionService.list_plans(db=db, active_only=active_only)


@router.post(
    "/",
    response_model=PlanRead,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(require_role("Doctor", "Admin", "Owner"))],
)
def create_plan(
    plan_in: PlanCreate,
    current_user: Annotated[User, Depends(get_current_user)],
    db: Annotated[Session, Depends(get_db)],
):
    doctor_profile = DoctorService.get_by_user_id(db=db, user_id=current_user.id)
    doctor_id = doctor_profile.id if doctor_profile else plan_in.doctor_id
    plan = SubscriptionService.create_plan(db=db, plan_in=plan_in, doctor_id=doctor_id)
    AuditService.log(
        db=db,
        user_id=current_user.id,
        action="CREATE_PLAN",
        entity="Plan",
        entity_id=str(plan.id),
    )
    return plan


@router.put(
    "/{plan_id}",
    response_model=PlanRead,
    dependencies=[Depends(require_role("Doctor", "Admin", "Owner"))],
)
def update_plan(
    plan_id: int,
    plan_in: PlanUpdate,
    db: Annotated[Session, Depends(get_db)],
):
    return SubscriptionService.update_plan(db=db, plan_id=plan_id, plan_in=plan_in)
