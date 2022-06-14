from typing import Union, Optional

from pydantic import BaseModel

from .base import BaseError

class ProblemNotFoundError(BaseError):
    CODE: int = 404

    def __init__(self, slug: Optional[str] = None, id: Optional[int] = None):
        super().__init__(ProblemNotFoundError, slug if slug else id, "Problem not found") 