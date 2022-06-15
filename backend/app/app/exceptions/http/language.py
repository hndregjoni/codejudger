from typing import Optional

from fastapi import status

from .base import BaseError

class LanguageNotFoundError(BaseError):
    CODE: int = status.HTTP_404_NOT_FOUND

    def __init__(self, lang: str):
        super().__init__(LanguageNotFoundError, lang, "Language not found") 