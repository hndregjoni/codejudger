from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Table
from sqlalchemy.orm import relationship

from app.db.base_class import Base
from app.db.mixins import TimestampedMixin

judger_language = Table(
    "judgerlanguage",
    Base.metadata,
    Column("judger_id", ForeignKey("judger.id"), primary_key=True),
    Column("language_id", ForeignKey("language.id"), primary_key=True)
)

class Judger(Base, TimestampedMixin):
    id = Column(Integer, primary_key=True, index=True)

    created_by_id = Column(Integer, ForeignKey("user.id"))
    created_by = relationship("User")

    host = Column(String(length=255))
    port = Column(Integer)

    languages_supported = relationship("Judger", back_populates="supported_by")