from typing import Optional

from fastapi import status

from .base import BaseError

class UserNotFoundError(BaseError):
    CODE: int = status.HTTP_404_NOT_FOUND

    def __init__(self, username: Optional[str] = None, id: Optional[int] = None):
        super().__init__(UserNotFoundError, username if username else id, "User not found") 

class UserExistsError(BaseError):
    CODE: int = status.HTTP_400_BAD_REQUEST

    def __init__(self, user: str):
        super().__init__(UserExistsError, user, "User already exists") 