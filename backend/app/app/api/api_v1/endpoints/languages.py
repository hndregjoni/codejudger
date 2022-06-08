from typing import Any, List

from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session


from app import crud, models, schemas
from app.api import deps

router = APIRouter()

@router.get("/", response_model=List[schemas.LanguageBase])
def get_languages(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100
) -> Any:
    return crud.language.get_multi(db, skip=skip, limit=limit)