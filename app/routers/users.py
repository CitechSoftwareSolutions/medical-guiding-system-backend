from typing import Annotated, List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload

from app.core.deps import get_db, require_role, get_current_user
from app.models.user import User
from app.schemas.auth import UserRead

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/", response_model=List[UserRead], dependencies=[Depends(require_role("Admin", "Owner"))])
def list_users(
    db: Annotated[Session, Depends(get_db)],
    skip: int = 0,
    limit: int = 50,
):
    stmt = (
        select(User)
        .options(selectinload(User.user_roles))
        .offset(skip)
        .limit(limit)
    )
    return list(db.scalars(stmt).all())


@router.get("/{user_id}", response_model=UserRead)
def get_user(
    user_id: int,
    db: Annotated[Session, Depends(get_db)],
    current_user: Annotated[User, Depends(get_current_user)],
):
    # Allow user to view their own profile or admin
    user_roles = [ur.role.name for ur in current_user.user_roles if ur.role]
    if current_user.id != user_id and "Admin" not in user_roles and "Owner" not in user_roles:
        raise HTTPException(status_code=403, detail="Not authorized to view this user")
    user = db.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.put("/{user_id}/status", dependencies=[Depends(require_role("Admin", "Owner"))])
def update_user_status(
    user_id: int,
    status_value: str,
    db: Annotated[Session, Depends(get_db)],
):
    user = db.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user.status = status_value
    db.commit()
    return {"message": f"User status updated to {status_value}", "user_id": user_id}
