from typing import Optional

from pydantic import BaseModel

class LanguageBase(BaseModel):
    id: str
    name: str

class LanguageShort(LanguageBase):
    class Config:
        orm_mode = True

class Language(LanguageBase):
    placeholder: str

    class Config:
        orm_mode = True

class LanguageCreate(Language):
    pass

class LanguageUpdate(BaseModel):
    name: str
    placeholder: str