import os
import shutil
import time
from typing import Annotated, List
from fastapi import APIRouter, Depends, HTTPException, status, Request, UploadFile, File
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.config import settings
from app.core.deps import get_db, get_current_user, require_role
from app.core.security import create_access_token
from app.models.user import User
from app.models.role import Role, Permission
from app.schemas.auth import (
    UserRegister,
    UserLogin,
    Token,
    UserRead,
    RoleRead,
    PermissionRead,
    UserRoleAssign,
    PasswordChange,
    UserUpdate,
)
from app.services.auth_service import AuthService
from app.services.audit_service import AuditService

router = APIRouter(prefix="/auth", tags=["Authentication & RBAC"])


@router.post("/register", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def register(
    user_in: UserRegister,
    db: Annotated[Session, Depends(get_db)],
    request: Request,
):
    user = AuthService.register_user(db=db, user_in=user_in)
    AuditService.log(
        db=db,
        user_id=user.id,
        action="REGISTER",
        entity="User",
        entity_id=str(user.id),
        ip_address=request.client.host if request.client else None,
    )
    return user


@router.post("/login", response_model=Token)
def login(
    user_in: UserLogin,
    db: Annotated[Session, Depends(get_db)],
    request: Request,
):
    user = AuthService.authenticate_user(db=db, email=user_in.email, password=user_in.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    token = create_access_token(data={"sub": str(user.id), "email": user.email})
    AuditService.log(
        db=db,
        user_id=user.id,
        action="LOGIN",
        entity="User",
        entity_id=str(user.id),
        ip_address=request.client.host if request.client else None,
    )
    return Token(access_token=token, token_type="bearer")


@router.post("/login-token", response_model=Token, include_in_schema=False)
def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: Annotated[Session, Depends(get_db)],
):
    user = AuthService.authenticate_user(db=db, email=form_data.username, password=form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    token = create_access_token(data={"sub": str(user.id), "email": user.email})
    return Token(access_token=token, token_type="bearer")


@router.get("/me", response_model=UserRead)
def get_current_user_profile(
    current_user: Annotated[User, Depends(get_current_user)],
):
    return current_user


@router.put("/me", response_model=UserRead)
def update_current_user_profile(
    data: UserUpdate,
    current_user: Annotated[User, Depends(get_current_user)],
    db: Annotated[Session, Depends(get_db)],
):
    if data.first_name is not None:
        current_user.first_name = data.first_name.strip()
    if data.last_name is not None:
        current_user.last_name = data.last_name.strip()
    if data.phone is not None:
        current_user.phone = data.phone.strip() if data.phone else None
    if data.avatar_url is not None:
        current_user.avatar_url = data.avatar_url.strip() if data.avatar_url else None
    db.commit()
    db.refresh(current_user)
    AuditService.log(
        db=db,
        user_id=current_user.id,
        action="UPDATE_PROFILE",
        entity="User",
        entity_id=str(current_user.id),
    )
    return current_user


@router.post("/avatar", response_model=UserRead)
def upload_avatar(
    file: UploadFile = File(...),
    current_user: Annotated[User, Depends(get_current_user)] = None,
    db: Annotated[Session, Depends(get_db)] = None,
):
    allowed_extensions = {".jpg", ".jpeg", ".png", ".webp", ".gif"}
    _, ext = os.path.splitext(file.filename or "")
    if ext.lower() not in allowed_extensions:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Only image files (.jpg, .jpeg, .png, .webp, .gif) are supported.",
        )

    os.makedirs(settings.UPLOAD_DIR, exist_ok=True)
    clean_filename = f"avatar_{current_user.id}_{int(time.time())}{ext.lower()}"
    file_path = os.path.join(settings.UPLOAD_DIR, clean_filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    avatar_url = f"http://127.0.0.1:8000/uploads/{clean_filename}"
    current_user.avatar_url = avatar_url
    db.commit()
    db.refresh(current_user)

    AuditService.log(
        db=db,
        user_id=current_user.id,
        action="UPDATE_AVATAR",
        entity="User",
        entity_id=str(current_user.id),
    )
    return current_user




@router.post("/assign-role", dependencies=[Depends(require_role("Admin", "Owner"))])
def assign_role(
    data: UserRoleAssign,
    user_id: int,
    db: Annotated[Session, Depends(get_db)],
):
    user_role = AuthService.assign_role(db=db, user_id=user_id, role_id=data.role_id)
    AuditService.log(
        db=db,
        action="ASSIGN_ROLE",
        entity="UserRole",
        entity_id=str(user_role.id),
        user_id=user_id,
    )
    return {"message": "Role assigned successfully", "user_id": user_id, "role_id": data.role_id}


@router.get("/roles", response_model=List[RoleRead])
def list_roles(db: Annotated[Session, Depends(get_db)]):
    return list(db.scalars(select(Role)).all())


@router.get("/permissions", response_model=List[PermissionRead])
def list_permissions(db: Annotated[Session, Depends(get_db)]):
    return list(db.scalars(select(Permission)).all())


@router.post("/change-password")
def change_password(
    data: PasswordChange,
    current_user: Annotated[User, Depends(get_current_user)],
    db: Annotated[Session, Depends(get_db)],
):
    AuthService.change_password(
        db=db,
        user_id=current_user.id,
        old_pass=data.old_password,
        new_pass=data.new_password,
    )
    AuditService.log(
        db=db,
        user_id=current_user.id,
        action="CHANGE_PASSWORD",
        entity="User",
        entity_id=str(current_user.id),
    )
    return {"message": "Password updated successfully"}
