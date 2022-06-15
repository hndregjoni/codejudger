from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship

from app.db.base_class import Base
from app.db.mixins import TimestampedMixin

class Submission(Base, TimestampedMixin):
    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="submissions", uselist=False)

    problem_id = Column(Integer, ForeignKey("problem.id"))
    problem = relationship("Problem", foreign_keys=[problem_id], uselist=False)

    attempt = relationship("ProblemAttempt", foreign_keys=[user_id, problem_id], uselist=False)

    code = Column(String(20000))

    # The judger that went through with the evaluation
    judger_id = Column(Integer, ForeignKey("judger.id"))
    judger = relationship("Judger", foreign_keys=[judger_id], uselist=False)

    # Has evaluation finished
    evaluated = Column(Boolean, default=False)

    evaluation_begin = Column(DateTime, nullable=True)
    evaluation_end = Column(DateTime, nullable=True)

    # The language used
    language_id = Column(String, ForeignKey("language.id"))
    language = relationship("Language", foreign_keys=[language_id], uselist=False)

    # Timing results
    passed = Column(Integer)
    failed = Column(Integer)

    failed_wrong = Column(Integer)
    failed_time = Column(Integer)
    failed_space = Column(Integer)
    failed_syntax = Column(Integer)
    failed_other = Column(Integer)

    weighted_sum = Column(Integer)