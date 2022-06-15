from typing import Optional

from fastapi import status

from .base import BaseError

class ProblemNotFoundError(BaseError):
    CODE: int = status.HTTP_404_NOT_FOUND

    def __init__(self, slug: Optional[str] = None, id: Optional[int] = None):
        super().__init__(ProblemNotFoundError, slug if slug else id, "Problem not found") 

class CannotAttemptError(BaseError):
    CODE: int = status.HTTP_403_FORBIDDEN

    def __init__(self, slug: Optional[str] = None, id: Optional[int] = None):
        super().__init__(CannotAttemptError, slug if slug else id, "Problem cannot be attempted by user") 