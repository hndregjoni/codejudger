from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from app.db.base_class import Base

class SpaceTimeConstraint(Base):
    id = Column(Integer, primary_key=True)

    cset_id = Column(Integer, ForeignKey("constraintset.id", use_alter=True))
    # cset = relationship("ConstraintSet", back_populates="spacetime_constraint", foreign_keys=[cset_id], uselist=False)

    # Time in milliseconds
    time = Column(Integer, nullable=True)
    # Space in MB
    space = Column(Integer, nullable=True)