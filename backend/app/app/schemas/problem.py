from typing import Optional, List, Tuple, Union, Set,  Any

from dataclasses import dataclass

from pydantic import BaseModel, validator
from pydantic.utils import GetterDict

from .tag import extract_slug

@dataclass
class TestCase:
    q: str
    a: str
    w: float
    v: bool

class ProblemConstraints(BaseModel):
    # List of users, string or id
    users: Optional[Union[List[str], List[int]]]
    time: Optional[float]
    space: Optional[int]

class ProblemBase(BaseModel):
    id: int
    slug: str

    title: str
    description: str

    # TODO: Fork
    soft_linked: bool
    head_commit: Optional[str]

    author_id = int


class ProblemCreate(BaseModel): 
    title: str
    description: str
    slug: Optional[str]

    test_cases: List[TestCase]
    @validator("test_cases")
    def validate_test_cases(cls, cases):
        if cases is None or len(cases)==0:
            raise ValueError("You must provide test cases")
        
        test_set: Set[str] = {}
        # Check for duplicates
        for case in cases:
            if case.a in test_set:
                raise ValueError(f"Test case duplicate: {case.a}")

    constraints: Optional[ProblemConstraints]
    tags: Optional[Union[List[str], List[int]]]

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