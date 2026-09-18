from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict
from app.schemas.category import CategoryRead


class DocumentBase(BaseModel):
    title: str
    description: Optional[str] = None
    category_id: Optional[int] = None
    visibility: Optional[str] = "free"  # 'free', 'premium', 'restricted'


class DocumentCreate(DocumentBase):
    file_url: str


class DocumentUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    category_id: Optional[int] = None
    visibility: Optional[str] = None
    file_url: Optional[str] = None


class DocumentRead(DocumentBase):
    id: int
    doctor_id: int
    file_url: str
    created_at: datetime
    updated_at: datetime
    category: Optional[CategoryRead] = None

    model_config = ConfigDict(from_attributes=True)


class StudentDocumentGrant(BaseModel):
    student_id: int
    document_id: int
    access_type: Optional[str] = "granted"  # 'free', 'purchased', 'granted'
    expires_at: Optional[datetime] = None


class StudentDocumentRead(BaseModel):
    id: int
    student_id: int
    document_id: int
    access_type: str
    granted_at: datetime
    expires_at: Optional[datetime] = None
    document: Optional[DocumentRead] = None

    model_config = ConfigDict(from_attributes=True)
