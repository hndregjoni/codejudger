from typing import Optional, List, Union

from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder

from app.crud.base import CRUDBase
from app.models.tag import Tag
from app.schemas.tag import TagCreate, TagUpdate
from app.schemas.tag import Tag as TagSchema
from app.exceptions import TagNotExistsError

class CRUDTag(CRUDBase[TagSchema, TagCreate, TagUpdate]):
    model: Tag

    def get_multi_poly(
        self, db: Session,
        identifiers: Union[List[int], List[str]]
    ) -> List[Tag]:
        result: List[Tag] = []

        if len(identifiers) == 0:
            return result

        if isinstance(identifiers[0], int):
            return self.get_multi_ids(db, identifiers)
        elif isinstance(identifiers[0], str):
            return self.get_multi_slugs(db, identifiers)

    def _check_all_tags(
        self,
        db_tags: List[Tag],
        identifiers: Union[List[int], List[str]]
    ) -> None:
        """ Throws error if some tags were not found """
        if len(db_tags) == len(identifiers):
            return
        
        for ident in identifiers:
            if not any([tag for tag in db_tags if tag.has_identifier(ident)]):
                raise TagNotExistsError(ident)

    def get_multi_slugs(self, db: Session, slugs: List[int]) -> List[Tag]:
        result = db.query(self.model).filter(self.model.slug.in_(slugs)).all()
        self._check_all_tags(result, slugs) 
        return result

    def get_multi_ids(self, db: Session, ids: List[int]) -> List[Tag]:
        result = db.query(self.model).filter(self.model.id.in_(ids)).all()
        self._check_all_tags(result, ids) 
        return result

    def get_with_slug(self, db: Session, slug: str) -> Optional[Tag]:
        """ Get an tag by its slug """
        return self.get_with_filter(db, self.model.slug == slug)
    
    def create_tag(self, db: Session, *, obj_in: TagCreate, author_id: int) -> Tag:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = Tag(**obj_in_data, author_id=author_id)  # type: ignore
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

tag = CRUDTag(Tag)