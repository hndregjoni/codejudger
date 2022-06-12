from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session


from app import crud, models, schemas
from app.api import deps
from app.schemas.language import LanguageCreate, LanguageUpdate

router = APIRouter()

@router.get("/", response_model=List[schemas.Tag])
def get_tags(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100
) -> Any:
    """ Get a list of tags """
    return crud.tag.get_multi(db, skip=skip, limit=limit)

@router.post("/", response_model=schemas.Tag)
def create_tag(
    *,
    db: Session = Depends(deps.get_db),
    tag_in: schemas.TagCreate,
    current_user: models.User = Depends(deps.get_current_active_user)
) -> Any:
    """ Create a tag """
    # Check whether tag with slug exists

    tag = crud.tag.get_with_slug(db, tag_in.slug)

    if tag:
        raise HTTPException(status_code=400, detail="Tag with the given slug already exists")
    
    created_tag = crud.tag.create_tag(
        db,
        obj_in=tag_in,
        author_id=current_user.id
    )

    return created_tag

@router.get("/id/{id}", response_model=schemas.Tag)
def get_tag_by_id(
    *,
    db: Session = Depends(deps.get_db),
    id: int
) -> Any:
    """ Get a tag by id """
    tag = crud.tag.get(db, id)

    if not tag:
        raise HTTPException(status_code=400, detail="Tag with the given id doesn't exist")
    
    return tag


@router.get("/slug/{slug}", response_model=schemas.Tag)
def get_tag_by_slug(
    *,
    db: Session = Depends(deps.get_db),
    slug: str
) -> Any:
    """ Get a tag by slug """
    tag = crud.tag.get_with_slug(db, slug)

    if not tag:
        raise HTTPException(status_code=400, detail="Tag with the given slug doesn't exist")
    
    return tag