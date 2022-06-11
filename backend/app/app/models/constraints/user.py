from enum import Enum

from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Table
from sqlalchemy.orm import relationship

from app.db.base_class import Base

UserConstraintType = Enum("UserConstraintType", "Whitelist Blacklist")

class UserConstraint(Base):
    id = Column(Integer, primary_key=True)

    cset_id = Column(Integer, ForeignKey("constraintset.id", use_alter=True))
    # cset = relationship("ConstraintSet", back_populates="user_constraints")

    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", backref="constrained_to")