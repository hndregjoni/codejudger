from typing import Optional

from fastapi import status

from .base import BaseError

from app.models import User, Problem
from app import models

class TagNotFoundError(BaseError):
    CODE: int = status.HTTP_404_NOT_FOUND

    def __init__(self, slug: Optional[str] = None):
        super().__init__(TagNotFoundError, slug , "Tag not found") 