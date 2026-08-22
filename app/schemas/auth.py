from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, EmailStr, ConfigDict


class PermissionRead(BaseModel):
    id: int
    name: str
    description: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)


class RoleRead(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    role_permissions: Optional[List["RolePermissionRead"]] = []

    model_config = ConfigDict(from_attributes=True)


class RolePermissionRead(BaseModel):
    permission: PermissionRead

    model_config = ConfigDict(from_attributes=True)


class UserRoleRead(BaseModel):
    role: RoleRead

    model_config = ConfigDict(from_attributes=True)


class UserRegister(BaseModel):
    email: EmailStr
    password: str
    first_name: str
    last_name: str
    phone: Optional[str] = None
    role: Optional[str] = "Student"  # Default registration role: 'Student' or 'Doctor'


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class TokenData(BaseModel):
    sub: Optional[str] = None


class UserRead(BaseModel):
    id: int
    email: EmailStr
    first_name: str
    last_name: str
    phone: Optional[str] = None
    status: str
    email_verified: bool
    created_at: datetime
    updated_at: datetime
    user_roles: List[UserRoleRead] = []

    model_config = ConfigDict(from_attributes=True)


class UserRoleAssign(BaseModel):
    role_id: int


class PasswordChange(BaseModel):
    old_password: str
    new_password: str
