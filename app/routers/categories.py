from typing import Annotated, List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.core.deps import get_db, require_role
from app.schemas.category import CategoryCreate, CategoryRead
from app.services.document_service import DocumentService

router = APIRouter(prefix="/categories", tags=["Document Categories"])


@router.get("/", response_model=List[CategoryRead])
def list_categories(db: Annotated[Session, Depends(get_db)]):
    return DocumentService.list_categories(db=db)


@router.post(
    "/",
    response_model=CategoryRead,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(require_role("Doctor", "Admin", "Owner"))],
)
def create_category(
    cat_in: CategoryCreate,
    db: Annotated[Session, Depends(get_db)],
):
    return DocumentService.create_category(db=db, cat_in=cat_in)
