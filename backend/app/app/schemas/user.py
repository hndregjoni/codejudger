from typing import Optional, List, Any

from pydantic import BaseModel, EmailStr, Field
from pydantic.utils import GetterDict

from .tag import Tag, extract_slug
from .role import UserRole, extract_role_name
from app.core.config import settings


# Shared properties
class UserBase(BaseModel):
    username: str = Field(..., regex=settings.USERNAME_REGEX)

    email: Optional[EmailStr] = None
    is_active: Optional[bool] = True
    is_superuser: bool = False
    full_name: Optional[str] = None


# Properties to receive via API on creation
class UserCreate(UserBase):
    email: EmailStr
    password: str


# Properties to receive via API on update
class UserUpdate(UserBase):
    password: Optional[str] = None
    interests: Optional[str] = None


class UserInDBBase(UserBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Very very hacky!
class UserGetter(GetterDict):
    def get(self, key: str, default: Any) -> Any:
        if key == "interests":
            return [*map(extract_slug, self._obj.interests)]
        
        if key == "roles":
            return [*map(extract_role_name, self._obj.roles)]
        
        return self._obj.__dict__[key]

class User(UserInDBBase):
    interests: List[str]
    roles: List[str]

    class Config:
        orm_mode = True
        getter_dict = UserGetter


# Additional properties stored in DB
class UserInDB(UserInDBBase):
    hashed_password: str