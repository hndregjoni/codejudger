from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session


from app import crud, models, schemas
from app.api import deps
from app.schemas.language import LanguageCreate, LanguageUpdate

router = APIRouter()

@router.get("/", response_model=List[schemas.LanguageShort])
def get_languages(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100
) -> Any:
    """ Get a list of the languages. """
    return crud.language.get_multi(db, skip=skip, limit=limit)

@router.post("/", response_model=schemas.Language)
def create_language(
    *,
    db: Session = Depends(deps.get_db),
    language_in: LanguageCreate,
    current_user: models.User = Depends(deps.get_current_active_user)
) -> Any:
    """ Create a language. """
    language = crud.language.create(db, obj_in=language_in)
    return language

@router.get("/{id}", response_model=schemas.Language)
def get_language(
    *,
    db: Session = Depends(deps.get_db),
    id: str
) -> Any:
    """ Get a single language """
    language = crud.language.get(db, id=id)
    
    if not language:
        raise HTTPException(status_code=404, detail="Language not found")
    
    return language


@router.put("/{id}", response_model=schemas.Language)
def update_language(
    *,
    db: Session = Depends(deps.get_db),
    id: str,
    language_in: LanguageUpdate,
    current_user: models.User = Depends(deps.get_current_active_user)
) -> Any:
    """ Update a language """
    language = crud.language.get(db, id)

    if not language:
        raise HTTPException(status_code=404, detail="Problem not found")
    
    #TODO: permissions

    language = crud.language.update(db=db, db_obj=language, obj_in=language_in)
    return language