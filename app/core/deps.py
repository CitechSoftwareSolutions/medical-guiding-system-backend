from typing import Annotated, Generator, List, Optional
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload

from app.core.config import settings
from app.core.security import decode_access_token
from app.db.database import get_db
from app.models.user import User
from app.models.role import UserRole, Role, RolePermission, Permission

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR}/auth/login-token",
    auto_error=False
)


def get_current_user(
    db: Annotated[Session, Depends(get_db)],
    token: Annotated[Optional[str], Depends(oauth2_scheme)],
) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    if not token:
        raise credentials_exception

    payload = decode_access_token(token)
    if payload is None:
        raise credentials_exception

    user_id = payload.get("sub")
    if user_id is None:
        raise credentials_exception

    stmt = (
        select(User)
        .where(User.id == int(user_id))
        .options(
            selectinload(User.doctor_profile),
            selectinload(User.student_profile),
            selectinload(User.user_roles)
            .selectinload(UserRole.role)
            .selectinload(Role.role_permissions)
            .selectinload(RolePermission.permission),
        )
    )
    user = db.scalar(stmt)
    if user is None:
        raise credentials_exception
    if user.status != "active":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Inactive user account",
        )
    return user


def get_optional_current_user(
    db: Annotated[Session, Depends(get_db)],
    token: Annotated[Optional[str], Depends(oauth2_scheme)],
) -> Optional[User]:
    if not token:
        return None
    try:
        return get_current_user(db=db, token=token)
    except HTTPException:
        return None


def require_role(*allowed_roles: str):
    def role_checker(current_user: Annotated[User, Depends(get_current_user)]) -> User:
        user_role_names = [ur.role.name for ur in current_user.user_roles if ur.role]
        if "Admin" in user_role_names or "Owner" in user_role_names:
            return current_user
        if not any(role in user_role_names for role in allowed_roles):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Access denied. Required roles: {', '.join(allowed_roles)}",
            )
        return current_user

    return role_checker


def require_permission(*required_permissions: str):
    def permission_checker(current_user: Annotated[User, Depends(get_current_user)]) -> User:
        user_role_names = [ur.role.name for ur in current_user.user_roles if ur.role]
        if "Admin" in user_role_names or "Owner" in user_role_names:
            return current_user

        user_permissions = set()
        for ur in current_user.user_roles:
            if ur.role:
                for rp in ur.role.role_permissions:
                    if rp.permission:
                        user_permissions.add(rp.permission.name)

        if not any(perm in user_permissions for perm in required_permissions):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Access denied. Required permissions: {', '.join(required_permissions)}",
            )
        return current_user

    return permission_checker
