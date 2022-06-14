from sqlalchemy import Column, ForeignKey, Integer, Table
from sqlalchemy.orm import relationship

from app.db.base_class import Base


# This entity connects many SpaceTimeConstraints with many Languages
spacetimelanguages = Table(
    "spacetimelanguages",
    Base.metadata,
    Column('spacetimeconstraint_id', ForeignKey("spacetimeconstraint.id"), primary_key=True),
    Column('language_id', ForeignKey("language.id"), primary_key=True)
)

class SpaceTimeConstraint(Base):
    id = Column(Integer, primary_key=True)

    cset_id = Column(Integer, ForeignKey("constraintset.id", use_alter=True), nullable=True)
    cset = relationship("ConstraintSet", back_populates="spacetime_constraints", foreign_keys=[cset_id], uselist=False)

    # Time in milliseconds
    time = Column(Integer, nullable=True)
    # Space in MB
    space = Column(Integer, nullable=True)

    language = relationship("Language", secondary=spacetimelanguages)