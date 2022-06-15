from typing import Optional

from fastapi import status

from .base import BaseError

class UserExistsError(BaseError):
    CODE: int = status.HTTP_404_NOT_FOUND

    def __init__(self, user: str):
        super().__init__(UserExistsError, user, "User already exists") 