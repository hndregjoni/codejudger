from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Table
from sqlalchemy.orm import relationship

from app.db.base_class import Base

class ConstraintSet(Base):
    id = Column(Integer, primary_key=True)

    spacetime_constraint_id = Column(Integer, ForeignKey("spacetimeconstraint.id", use_alter=True))
    spacetime_constraint = relationship("SpaceTimeConstraint", backref="cset", uselist=False, foreign_keys=[spacetime_constraint_id])

    timespan_constraint_id = Column(Integer, ForeignKey("timespanconstraint.id", use_alter=True))
    timespan_constraint = relationship("TimespanConstraint", backref="cset", uselist=False, foreign_keys=[timespan_constraint_id])

    language_constraints = relationship("LanguageConstraint", backref="cset")
    user_constraints = relationship("UserConstraint", backref="cset")

    # TODO: team constraint when teams make it in