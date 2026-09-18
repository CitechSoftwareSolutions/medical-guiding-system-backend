from typing import List, Optional, Annotated
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.deps import get_db, get_current_user, require_role
from app.models.user import User
from app.models.navigation import NavigationItem
from app.schemas.navigation import NavigationItemCreate, NavigationItemUpdate, NavigationItemRead

router = APIRouter(prefix="/navigation", tags=["Navigation"])


@router.get("/", response_model=List[NavigationItemRead])
def list_navigation_items(
    db: Annotated[Session, Depends(get_db)],
    menu_type: Optional[str] = Query(None, description="e.g. top_navbar, sidebar_student, sidebar_doctor, sidebar_admin"),
    target_role: Optional[str] = Query(None, description="e.g. public, student, doctor, admin, all"),
    active_only: bool = Query(True, description="Filter only active items"),
):
    stmt = select(NavigationItem)
    if active_only:
        stmt = stmt.where(NavigationItem.is_active.is_(True))
    if menu_type:
        stmt = stmt.where(NavigationItem.menu_type == menu_type)
    if target_role and target_role != "all":
        stmt = stmt.where(NavigationItem.target_role.in_([target_role, "all"]))

    stmt = stmt.order_by(NavigationItem.display_order.asc(), NavigationItem.id.asc())
    return list(db.scalars(stmt).all())


@router.post("/", response_model=NavigationItemRead, status_code=status.HTTP_201_CREATED)
def create_navigation_item(
    item_in: NavigationItemCreate,
    current_user: Annotated[User, Depends(require_role("Admin", "Owner"))],
    db: Annotated[Session, Depends(get_db)],
):
    new_item = NavigationItem(
        title=item_in.title,
        path=item_in.path,
        icon=item_in.icon,
        menu_type=item_in.menu_type,
        target_role=item_in.target_role,
        display_order=item_in.display_order,
        is_active=item_in.is_active,
    )
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item


@router.put("/{item_id}", response_model=NavigationItemRead)
def update_navigation_item(
    item_id: int,
    item_in: NavigationItemUpdate,
    current_user: Annotated[User, Depends(require_role("Admin", "Owner"))],
    db: Annotated[Session, Depends(get_db)],
):
    item = db.get(NavigationItem, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Navigation item not found")

    update_data = item_in.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(item, field, value)

    db.commit()
    db.refresh(item)
    return item


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_navigation_item(
    item_id: int,
    current_user: Annotated[User, Depends(require_role("Admin", "Owner"))],
    db: Annotated[Session, Depends(get_db)],
):
    item = db.get(NavigationItem, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Navigation item not found")

    db.delete(item)
    db.commit()
    return None
