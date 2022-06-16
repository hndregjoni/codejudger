from typing import TYPE_CHECKING

from enum import Enum

from sqlalchemy import Boolean, Column, Integer, String, Table, ForeignKey
from sqlalchemy import Enum as _Enum
from sqlalchemy.orm import relationship

from app.db.base_class import Base
from app.db.mixins import TimestampedMixin

if TYPE_CHECKING:
    from .item import Item  # noqa: F401

user_roles = Table(
    "userroles",
    Base.metadata,
    Column('user_id', ForeignKey("user.id"), primary_key=True),
    Column('role_id', ForeignKey("userrole.id"), primary_key=True)
)

user_interests = Table(
    "userinterests",
    Base.metadata,
    Column('user_id', ForeignKey("user.id"), primary_key=True),
    Column('tag_id', ForeignKey("tag.id"), primary_key=True)
)

Gender = Enum("Gender", "Male Female Other NotSpecified")

class User(Base, TimestampedMixin):
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    full_name = Column(String, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)

    items = relationship("Item", back_populates="owner")

    roles = relationship("UserRole", secondary=user_roles)
    interests = relationship("Tag", secondary=user_interests)

    problems_authored = relationship("Problem", back_populates="author")
    attempts = relationship("ProblemAttempt", back_populates="user")

    submissions = relationship("Submission", back_populates="user")

    # Additional profile information
    bio = Column(String(200))
    gender = Column(_Enum(Gender))

    # Eventually a profile picture:

    activated_once = Column(Boolean, default=False)