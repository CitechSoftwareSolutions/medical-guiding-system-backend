from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, ConfigDict


class PlanBase(BaseModel):
    name: str
    price: float
    duration_days: int = 30
    description: Optional[str] = None
    features: Optional[List[str]] = None


class PlanCreate(PlanBase):
    doctor_id: Optional[int] = None


class PlanUpdate(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    duration_days: Optional[int] = None
    description: Optional[str] = None
    features: Optional[List[str]] = None
    status: Optional[str] = None


class PlanRead(PlanBase):
    id: int
    doctor_id: Optional[int] = None
    status: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
