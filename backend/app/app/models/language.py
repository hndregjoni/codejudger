from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import deferred, relationship

from app.db.base_class import Base
from app.db.mixins import TimestampedMixin

from .judger import judger_language

class Language(Base, TimestampedMixin):
    id = Column(String(length=60), primary_key=True, index=True)

    name = Column(String(length=80), unique=True)

    placeholder = deferred(Column(String(2000)))

    supported_by = relationship("Judger", secondary=judger_language, back_populates="languages_supported")

    spacetime_constraint_id = Column(Integer, ForeignKey("spacetimeconstraint.id"))
    spacetime_constraint = relationship("SpacetimeConstraint")