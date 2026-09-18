from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict


class NavigationItemBase(BaseModel):
    title: str
    path: str
    icon: Optional[str] = None
    menu_type: str = "top_navbar"  # 'top_navbar', 'sidebar_student', 'sidebar_doctor', 'sidebar_admin', 'footer'
    target_role: str = "all"  # 'public', 'student', 'doctor', 'admin', 'all'
    display_order: int = 0
    is_active: bool = True


class NavigationItemCreate(NavigationItemBase):
    pass


class NavigationItemUpdate(BaseModel):
    title: Optional[str] = None
    path: Optional[str] = None
    icon: Optional[str] = None
    menu_type: Optional[str] = None
    target_role: Optional[str] = None
    display_order: Optional[int] = None
    is_active: Optional[bool] = None


class NavigationItemRead(NavigationItemBase):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
