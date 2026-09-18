from typing import Annotated, List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.deps import get_db, get_current_user
from app.models.user import User
from app.schemas.notification import NotificationRead
from app.services.notification_service import NotificationService

router = APIRouter(prefix="/notifications", tags=["Notifications"])


@router.get("/", response_model=List[NotificationRead])
def get_my_notifications(
    current_user: Annotated[User, Depends(get_current_user)],
    db: Annotated[Session, Depends(get_db)],
    unread_only: bool = False,
):
    return NotificationService.list_user_notifications(
        db=db, user_id=current_user.id, unread_only=unread_only
    )


@router.put("/mark-all-read")
def mark_all_notifications_read(
    current_user: Annotated[User, Depends(get_current_user)],
    db: Annotated[Session, Depends(get_db)],
):
    count = NotificationService.mark_all_as_read(db=db, user_id=current_user.id)
    return {"message": f"{count} notifications marked as read", "count": count}


@router.put("/{notification_id}/read", response_model=NotificationRead)
def mark_notification_read(
    notification_id: int,
    current_user: Annotated[User, Depends(get_current_user)],
    db: Annotated[Session, Depends(get_db)],
):
    return NotificationService.mark_as_read(
        db=db, notification_id=notification_id, user_id=current_user.id
    )


@router.put("/{notification_id}/unread", response_model=NotificationRead)
def mark_notification_unread(
    notification_id: int,
    current_user: Annotated[User, Depends(get_current_user)],
    db: Annotated[Session, Depends(get_db)],
):
    return NotificationService.mark_as_unread(
        db=db, notification_id=notification_id, user_id=current_user.id
    )


@router.delete("/{notification_id}")
def delete_notification(
    notification_id: int,
    current_user: Annotated[User, Depends(get_current_user)],
    db: Annotated[Session, Depends(get_db)],
):
    NotificationService.delete_notification(
        db=db, notification_id=notification_id, user_id=current_user.id
    )
    return {"message": "Notification deleted successfully"}


@router.delete("/")
def clear_notifications(
    current_user: Annotated[User, Depends(get_current_user)],
    db: Annotated[Session, Depends(get_db)],
    read_only: bool = False,
):
    count = NotificationService.clear_all(db=db, user_id=current_user.id, read_only=read_only)
    return {"message": f"{count} notifications deleted", "count": count}
