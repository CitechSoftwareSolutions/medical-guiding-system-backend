from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict
from app.schemas.plan import PlanRead


class SubscriptionCreate(BaseModel):
    plan_id: int
    payment_id: Optional[int] = None


class SubscriptionUpdate(BaseModel):
    status: Optional[str] = None
    end_date: Optional[datetime] = None


class SubscriptionRead(BaseModel):
    id: int
    student_id: int
    plan_id: int
    payment_id: Optional[int] = None
    status: str
    start_date: datetime
    end_date: datetime
    created_at: datetime
    updated_at: datetime
    plan: Optional[PlanRead] = None

    model_config = ConfigDict(from_attributes=True)
