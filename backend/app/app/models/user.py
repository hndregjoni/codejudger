from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base
from app.db.mixins import TimestampedMixin

if TYPE_CHECKING:
    from .item import Item  # noqa: F401

user_roles = Table(
    "userroles",
    Base.metadata,
    Column('user_id', ForeignKey("user.id"), primary_key=True, unique=True),
    Column('role_id', ForeignKey("userrole.id"), unique=True, primary_key=True)
)

class User(Base, TimestampedMixin):
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)

    items = relationship("Item", back_populates="owner")

    roles = relationship("UserRole", secondary=user_roles)

    problems_authored = relationship("Problem", back_populates="author")
    attempts = relationship("ProblemAttempt", back_populates="user")