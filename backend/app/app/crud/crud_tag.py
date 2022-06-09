from tkinter import W
from typing import Optional

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.tag import Tag
from app.schemas.tag import TagCreate, TagUpdate
from app.schemas.tag import Tag as TagSchema

class CRUDTag(CRUDBase[TagSchema, TagCreate, TagUpdate]):
    model: Tag
    
    def get_with_slug(self, db: Session, slug: str) -> Optional[Tag]:
        """ Get an tag by its slug """
        return self.get_with_filter(db, self.model.slug == slug)

tag = CRUDTag(Tag)