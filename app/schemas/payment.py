from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict


class PaymentBase(BaseModel):
    amount: float
    currency: Optional[str] = "USD"
    gateway: Optional[str] = "manual"
    transaction_id: Optional[str] = None


class PaymentCreate(PaymentBase):
    plan_id: Optional[int] = None


class PaymentUpdate(BaseModel):
    status: str
    transaction_id: Optional[str] = None


class PaymentRead(PaymentBase):
    id: int
    student_id: int
    plan_id: Optional[int] = None
    status: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
