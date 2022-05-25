from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship

from app.db.base_class import Base
from app.db.mixins import TimestampedMixin

class Tag(Base, TimestampedMixin):
    id = Column(Integer, primary_key=True, index=True)
    slug = Column(String(length=60), unique=True, index=True)
    
    title = Column(String, index=True)

    created_by_id = Column(Integer, ForeignKey("user.id"))
    created_by = relationship("User")