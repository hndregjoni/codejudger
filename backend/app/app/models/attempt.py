from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from app.db.base_class import Base

class ProblemAttempt(Base):
    # Side of the user
    user_id = Column(Integer, ForeignKey("user.id"), primary_key=True, unique=True)
    user = relationship("User", back_populates="attempts")

    # Side of the problem
    problem_id = Column(Integer, ForeignKey("problem.id"), primary_key=True, unique=True)
    problem = relationship("Problem", back_populates="attempts")

    # Data pertainting to the relationship between a user and a problem
    first_submission_id = Column(Integer, ForeignKey("submission.id"))
    effective_submission_id = Column(Integer, ForeignKey("submission.id"))
    active_submission_id = Column(Integer, ForeignKey("submission.id"))