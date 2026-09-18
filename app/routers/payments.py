from typing import Annotated, List, Optional
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.deps import get_db, get_current_user, require_role
from app.models.user import User
from app.schemas.payment import PaymentCreate, PaymentRead
from app.services.payment_service import PaymentService
from app.services.student_service import StudentService
from app.services.audit_service import AuditService

router = APIRouter(prefix="/payments", tags=["Payments"])


@router.post("/", response_model=PaymentRead, status_code=status.HTTP_201_CREATED)
def make_payment(
    payment_in: PaymentCreate,
    current_user: Annotated[User, Depends(get_current_user)],
    db: Annotated[Session, Depends(get_db)],
):
    student_profile = StudentService.get_by_user_id(db=db, user_id=current_user.id)
    if not student_profile:
        raise HTTPException(status_code=400, detail="Only students can initiate payment transactions")

    payment = PaymentService.create_payment(
        db=db, student_id=student_profile.id, payment_in=payment_in
    )
    AuditService.log(
        db=db,
        user_id=current_user.id,
        action="PROCESS_PAYMENT",
        entity="Payment",
        entity_id=str(payment.id),
    )
    return payment


@router.get("/my-payments", response_model=List[PaymentRead])
def list_my_payments(
    current_user: Annotated[User, Depends(get_current_user)],
    db: Annotated[Session, Depends(get_db)],
    skip: int = 0,
    limit: int = 50,
):
    student_profile = StudentService.get_by_user_id(db=db, user_id=current_user.id)
    if not student_profile:
        raise HTTPException(status_code=400, detail="Current user is not a student")
    return PaymentService.list_payments(db=db, student_id=student_profile.id, skip=skip, limit=limit)


@router.get("/", response_model=List[PaymentRead], dependencies=[Depends(require_role("Admin", "Owner"))])
def list_all_payments(
    db: Annotated[Session, Depends(get_db)],
    skip: int = 0,
    limit: int = 50,
):
    return PaymentService.list_payments(db=db, skip=skip, limit=limit)
