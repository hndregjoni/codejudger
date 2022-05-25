from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Table
from sqlalchemy.orm import relationship

from app.db.base_class import Base
from app.db.mixins import TimestampedMixin

from .judger import judger_language

class Language(Base, TimestampedMixin):
    id = Column(String(length=60), primary_key=True, index=True)

    name = Column(String(length=80), unique=True)

    supported_by = relationship("Judger", secondary=judger_language, back_populates="languages_supported")