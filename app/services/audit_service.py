from typing import List, Optional
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.audit import AuditLog


class AuditService:
    @staticmethod
    def log(
        db: Session,
        action: str,
        entity: str,
        entity_id: Optional[str] = None,
        user_id: Optional[int] = None,
        ip_address: Optional[str] = None,
    ) -> AuditLog:
        log_entry = AuditLog(
            user_id=user_id,
            action=action,
            entity=entity,
            entity_id=str(entity_id) if entity_id is not None else None,
            ip_address=ip_address,
        )
        db.add(log_entry)
        db.commit()
        db.refresh(log_entry)
        return log_entry

    @staticmethod
    def list_logs(
        db: Session,
        user_id: Optional[int] = None,
        action: Optional[str] = None,
        skip: int = 0,
        limit: int = 50,
    ) -> List[AuditLog]:
        stmt = select(AuditLog)
        if user_id:
            stmt = stmt.where(AuditLog.user_id == user_id)
        if action:
            stmt = stmt.where(AuditLog.action == action)
        return list(db.scalars(stmt.order_by(AuditLog.created_at.desc()).offset(skip).limit(limit)).all())
