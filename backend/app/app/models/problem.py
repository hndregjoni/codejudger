from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Table
from sqlalchemy.orm import relationship

from app.db.base_class import Base
from app.db.mixins import TimestampedMixin

problem_tags = Table(
    "problemtags",
    Base.metadata,
    Column('problem_id', ForeignKey("problem.id"), primary_key=True, unique=True),
    Column('tag_id', ForeignKey("tag.id"), unique=True, primary_key=True)
)

class Problem(Base, TimestampedMixin):
    id = Column(Integer, primary_key=True, index=True)
    slug = Column(String(length=60), index=True, unique=True)

    title = Column(String, index=True)
    description = Column(String)
    tags = relationship("Tag", secondary=problem_tags)

    # git
    fork_of_id = Column(Integer)
    fork_of = relationship("Problem", back_populates="forks")
    forks = relationship("Problem", back_populates="fork_of")

    soft_linked = Column(Boolean, default=False)
    head_commit = Column(String(length=40), index=True)

    # Problem author
    author_id = Column(Integer, ForeignKey("user.id"))
    author = relationship("User", back_populates="problems_authored")

    attempts = relationship("ProblemAttempt", back_populates="problem")