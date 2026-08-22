from typing import List
from sqlalchemy import select
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.models.notification import Notification


class NotificationService:
    @staticmethod
    def send_notification(
        db: Session, user_id: int, title: str, body: str
    ) -> Notification:
        notif = Notification(user_id=user_id, title=title, body=body, is_read=False)
        db.add(notif)
        db.commit()
        db.refresh(notif)
        return notif

    @staticmethod
    def list_user_notifications(
        db: Session, user_id: int, unread_only: bool = False
    ) -> List[Notification]:
        stmt = select(Notification).where(Notification.user_id == user_id)
        if unread_only:
            stmt = stmt.where(Notification.is_read == False)
        return list(db.scalars(stmt.order_by(Notification.created_at.desc())).all())

    @staticmethod
    def mark_as_read(db: Session, notification_id: int, user_id: int) -> Notification:
        notif = db.get(Notification, notification_id)
        if not notif or notif.user_id != user_id:
            raise HTTPException(status_code=404, detail="Notification not found")
        notif.is_read = True
        db.commit()
        db.refresh(notif)
        return notif
