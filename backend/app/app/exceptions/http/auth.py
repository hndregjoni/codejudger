from typing import Optional

from fastapi import status

from .base import BaseError

class UserInactiveError(BaseError):
    CODE: int = status.HTTP_403_FORBIDDEN

    def __init__(self, user: str):
        super().__init__(UserInactiveError, user, "User is inactive") 

class NoOpenUserRegistrationError(BaseError):
    CODE: int = status.HTTP_401_UNAUTHORIZED

    def __init__(self):
        super().__init__(NoOpenUserRegistrationError, "", "Open registration is disabled")