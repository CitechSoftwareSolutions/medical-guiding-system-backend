from datetime import datetime
from typing import Optional
from sqlalchemy import String, Integer, Boolean, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column

from app.db.database import Base


class NavigationItem(Base):
    __tablename__ = "navigation_items"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    path: Mapped[str] = mapped_column(String(255), nullable=False)
    icon: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    menu_type: Mapped[str] = mapped_column(
        String(50), default="top_navbar", server_default="top_navbar", nullable=False, index=True
    )  # 'top_navbar', 'sidebar_student', 'sidebar_doctor', 'sidebar_admin', 'footer'
    target_role: Mapped[str] = mapped_column(
        String(50), default="all", server_default="all", nullable=False, index=True
    )  # 'public', 'student', 'doctor', 'admin', 'all'
    display_order: Mapped[int] = mapped_column(Integer, default=0, server_default="0", nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, server_default="true", nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    def __repr__(self) -> str:
        return f"<NavigationItem(id={self.id}, title='{self.title}', menu_type='{self.menu_type}', path='{self.path}')>"
