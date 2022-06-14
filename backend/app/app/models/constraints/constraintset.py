from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Table, Enum
from sqlalchemy.orm import relationship

from app.db.base_class import Base
from .user import UserConstraintType

from .filter import FilterType

class ConstraintSet(Base):
    id = Column(Integer, primary_key=True)

    # spacetime_constraint_id = Column(Integer, ForeignKey("spacetimeconstraint.id", use_alter=True))

    timespan_constraint_id = Column(Integer, ForeignKey("timespanconstraint.id", use_alter=True))
    timespan_constraint = relationship("TimespanConstraint", backref="cset", uselist=False, foreign_keys=[timespan_constraint_id])

    spacetime_constraints = relationship("SpaceTimeConstraint", backref="cset")
    l_filter_type = Column(Enum(FilterType), nullable=True)
    language_constraints = relationship("LanguageConstraint", backref="cset")
    u_filter_type = Column(Enum(FilterType), nullable=True)
    user_constraints = relationship("UserConstraint", backref="cset")

    user_constraint_type = Column(Enum(UserConstraintType), nullable=True)

    # TODO: team constraint when teams make it in