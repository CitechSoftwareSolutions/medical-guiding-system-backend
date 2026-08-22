from typing import Annotated, List, Optional
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.deps import get_db, require_role
from app.schemas.audit import AuditLogRead
from app.services.audit_service import AuditService

router = APIRouter(prefix="/audit-logs", tags=["Audit Logs"])


@router.get("/", response_model=List[AuditLogRead], dependencies=[Depends(require_role("Admin", "Owner"))])
def list_audit_logs(
    db: Annotated[Session, Depends(get_db)],
    user_id: Optional[int] = None,
    action: Optional[str] = None,
    skip: int = 0,
    limit: int = 50,
):
    return AuditService.list_logs(db=db, user_id=user_id, action=action, skip=skip, limit=limit)
