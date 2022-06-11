from sqlalchemy import Column, ForeignKey, Integer, DateTime
from sqlalchemy.orm import relationship

from app.db.base_class import Base

class TimespanConstraint(Base):
    id = Column(Integer, primary_key=True)

    cset_id = Column(Integer, ForeignKey("constraintset.id", use_alter=True))
    # cset = relationship("ConstraintSet", back_populates="timespan_constraint")

    begin = Column(DateTime, nullable=True)
    end = Column(DateTime, nullable=True)