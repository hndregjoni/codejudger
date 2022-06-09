from typing import List


from sqlalchemy.orm import Session, defer

from app.crud.base import CRUDBase
from app.models.language import Language
from app.schemas.language import LanguageCreate, LanguageUpdate

class CRUDLanguage(CRUDBase[Language, LanguageCreate, LanguageUpdate]):
    pass

language = CRUDLanguage(Language)