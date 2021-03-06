from typing import Optional, List, Tuple, Union, Set,  Any

from dataclasses import dataclass

from pydantic import BaseModel, validator, Field
from pydantic.utils import GetterDict
from pydantic.dataclasses import dataclass

from .tag import extract_slug

from .util import _validate_test_cases
from app.core.config import settings


class TestCase(BaseModel):
    q: str
    a: str
    w: float
    v: bool

class SpaceTimeConstraint(BaseModel):
    time: int = Field(..., min=settings.MIN_TIME, max=settings.MAX_TIME)
    space: int = Field(..., min=settings.MIN_SPACE, max=settings.MAX_SPACE)
    languages: Optional[List[str]]


class ProblemConstraints(BaseModel):
    # List of users, string or id
    users: Optional[Union[List[str], List[int]]]

    spacetime: Optional[List[SpaceTimeConstraint]]
    @validator("spacetime")
    def validate_spacetime(cls, spacetime):
        if spacetime is not None and 0 < len(spacetime) <= settings.MAX_SPACETIME_CONSTRAINTS:
            raise ValueError(f"Spacetime Constraint limit should be between 0 and {settings.MAX_SPACETIME_CONSTRAINTS}")
        return spacetime

class ProblemBase(BaseModel):
    id: int
    slug: str

    title: str
    description: str = Field(..., max=20000)

    # TODO: Fork
    soft_linked: bool
    head_commit: Optional[str]
    is_forkable: bool

    author_id = int

    listed: bool
    disabled: bool
    frozen: bool


class ProblemCreate(BaseModel): 
    title: str
    description: str
    slug: Optional[str]

    test_cases: List[TestCase]
    @validator("test_cases")
    def validate_test_cases(cls, cases):
        return _validate_test_cases(cls, cases)

    constraints: Optional[ProblemConstraints]
    tags: Optional[Union[List[str], List[int]]]

    listed: bool
    frozen: bool

class ProblemStatement(BaseModel):
    statement: str

class ProblemUpdate(BaseModel):
    pass


class ProblemGetter(GetterDict):
    def get(self, key: str, default: Any) -> Any:
        if key == "tags":
            return [*map(extract_slug, self._obj.tags)]
        
        return self._obj.__dict__[key]

class Problem(ProblemBase):
    tags: List[str]

    class Config:
        orm_mode = True
        getter_dict = ProblemGetter