from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict
from app.schemas.auth import UserRead


class DoctorProfileBase(BaseModel):
    license_number: Optional[str] = None
    specialization: Optional[str] = None
    qualification: Optional[str] = None
    experience_years: Optional[int] = 0
    bio: Optional[str] = None


class DoctorProfileCreate(DoctorProfileBase):
    pass


class DoctorProfileUpdate(DoctorProfileBase):
    status: Optional[str] = None


class DoctorProfileRead(DoctorProfileBase):
    id: int
    user_id: int
    status: str
    created_at: datetime
    updated_at: datetime
    user: Optional[UserRead] = None

    model_config = ConfigDict(from_attributes=True)
