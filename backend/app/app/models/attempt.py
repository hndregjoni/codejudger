from collections import UserList
from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, ForeignKeyConstraint
from sqlalchemy.orm import relationship

from app.db.base_class import Base

class ProblemAttempt(Base):
    # Side of the user
    user_id = Column(Integer, ForeignKey("user.id"), primary_key=True, unique=True)
    user = relationship("User", back_populates="attempts", uselist=False)

    # Side of the problem
    problem_id = Column(Integer, ForeignKey("problem.id"), primary_key=True, unique=True)
    problem = relationship("Problem", back_populates="attempts", uselist=False)

    # List of submissions for this attempt:
    submissions = relationship("Submission", back_populates="attempt", primaryjoin="and_(ProblemAttempt.user_id==Submission.user_id,"
        "ProblemAttempt.problem_id==Submission.problem_id)")

    # Data pertainting to the relationship between a user and a problem
    first_submission_id = Column(Integer, ForeignKey("submission.id"))
    first_submission = relationship("Submission", foreign_keys=[first_submission_id], uselist=False)

    effective_submission_id = Column(Integer, ForeignKey("submission.id"))
    effective_submission = relationship("Submission", foreign_keys=[effective_submission_id], uselist=False)


    active_submission_id = Column(Integer, ForeignKey("submission.id"))
    active_submission = relationship("Submission", foreign_keys=[active_submission_id], uselist=False)