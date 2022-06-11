from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Table
from sqlalchemy.orm import relationship, backref

from app.db.base_class import Base
from app.db.mixins import TimestampedMixin

problem_tags = Table(
    "problemtags",
    Base.metadata,
    Column('problem_id', ForeignKey("problem.id"), primary_key=True),
    Column('tag_id', ForeignKey("tag.id"), primary_key=True)
)

class Problem(Base, TimestampedMixin):
    id = Column(Integer, primary_key=True, index=True)
    slug = Column(String(length=60), index=True, unique=True)

    title = Column(String(length=180), index=True)
    
    # Set a lmit to 20k characters for a problem description
    description = Column(String(20000))

    tags = relationship("Tag", secondary=problem_tags)

    # git
    fork_of_id = Column(Integer, ForeignKey("problem.id"))
    # fork_of = relationship("Problem", remote_side=[id])
    forks = relationship("Problem",
                backref=backref('fork_of', remote_side=[id])
            )

    soft_linked = Column(Boolean, default=False)
    head_commit = Column(String(length=40), index=True)
    is_forkable = Column(Boolean, default=True)

    # Problem author
    author_id = Column(Integer, ForeignKey("user.id"))
    author = relationship("User", back_populates="problems_authored")

    attempts = relationship("ProblemAttempt", back_populates="problem")

    difficulty = Column(Integer)

    # The contest it's attached to:
    contest_id = Column(Integer, ForeignKey('contest.id'))
    contest = relationship("Contest", back_populates="problems")

    # The constraints:
    constraintset_id = Column(Integer, ForeignKey("constraintset.id"))
    constraintset = relationship("ConstraintSet", backref="constrained_problems")

    # Test case count:
    test_case_count = Column(Integer)