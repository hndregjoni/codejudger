from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union, Callable

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy import not_
from sqlalchemy.orm import Session, Query

from app.db.base_class import Base

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


not_disabled_func = lambda m: \
    lambda q: q.filter(not_(m.disabled))

class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    model: Type[ModelType]
    default_filter: Optional[Callable[[Query], Query]]

    def __init__(self, model: Type[ModelType]):
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD).

        **Parameters**

        * `model`: A SQLAlchemy model class
        * `schema`: A Pydantic model (schema) class
        """
        self.model = model
        self.default_filter = None

    def _with_filter(self, fltr: Callable[[Query], Query]) -> None:
        """ This chains filters """
        self.default_filter = fltr if not self.default_filter \
            else lambda q: fltr(self.default_filter(q))

    def _base_query(self, db: Session, apply_default: bool) -> Query:
        """ Returns a base query, that takes the default_filter into consideration """
        query = db.query(self.model)

        if apply_default and self.default_filter:
            query = self.default_filter(query)
        
        return query


    def get(self, db: Session, id: Any, apply_default=True) -> Optional[ModelType]:
        query = self._base_query(db, apply_default)

        return query.filter(self.model.id == id).first()
    
    def get_with_filter(self, db: Session, *criterion: Any, apply_default=True) -> Optional[ModelType]:
        query = self._base_query(db, apply_default)

        return query.filter(*criterion).first()

    def get_multi(
        self, db: Session, *, skip: int = 0, limit: int = 100
    ) -> List[ModelType]:
        return db.query(self.model).offset(skip).limit(limit).all()

    def create(self, db: Session, *, obj_in: CreateSchemaType) -> ModelType:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)  # type: ignore
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self,
        db: Session,
        *,
        db_obj: ModelType,
        obj_in: Union[UpdateSchemaType, Dict[str, Any]]
    ) -> ModelType:
        obj_data = jsonable_encoder(db_obj)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def remove(self, db: Session, *, id: int) -> ModelType:
        obj = db.query(self.model).get(id)
        db.delete(obj)
        db.commit()
        return obj
    
    @staticmethod
    def paginate(query_in: Query, skip: int, limit: int) -> Query:
        return query_in.offset(skip).limit(limit)