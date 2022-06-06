from typing import TYPE_CHECKING

from enum import Enum

from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base
from app.db.mixins import TimestampedMixin

if TYPE_CHECKING:
    from .item import Item  # noqa: F401

UserRoles = Enum('UserRoles', "Admin Setter Solver")

class UserRole(Base, TimestampedMixin):
    id = Column(Integer, primary_key=True, index=True)

    role_name = Column(String(length=60), unique=True)