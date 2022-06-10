from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Table
from sqlalchemy.orm import relationship

from app.db.base_class import Base

from .language import LanguageConstraint
from .spacetime import SpaceTimeConstraint
from .timespan import TimespanConstraint
from .user import UserConstraint

class ConstraintSet(Base):
    id = Column(Integer, primary_key=True)

    spacetime_constraint_id = Column(Integer, ForeignKey("spacetimeconstraint.id", use_alter=True))
    spacetime_constraint = relationship("SpacetimeConstraint", back_populates="cset", uselist=False)

    timespan_constraint_id = Column(Integer, ForeignKey("timespanconstraint.id", use_alter=True))
    timespan_constraint = relationship("TimespanConstraint", back_populates="cset", uselist=False)

    language_constraints = relationship("LanguageConstraint", back_populates="cset")
    user_constraints = relationship("UserConstraint", back_populates="cset")

    # TODO: team constraint when teams make it in