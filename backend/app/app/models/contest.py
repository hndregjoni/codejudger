from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Table
from sqlalchemy.orm import relationship, backref

from app.db.base_class import Base
from app.db.mixins import TimestampedMixin

class Contest(Base):
    id = Column(Integer, primary_key=True, index=True)
    slug = Column(String(length=60), index=True, unique=True)

    title = Column(String(length=180))

    # Problems part of this contest
    problems = relationship("Problem", back_populates="contest")

    # ConstraintSet for this contest
    cset_id = Column(Integer, ForeignKey("constraintset.id"))
    cset = relationship("ConstraintSet")