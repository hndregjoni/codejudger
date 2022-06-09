from typing import Optional

from pydantic import BaseModel

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
    pass

class ProblemUpdate(BaseModel):
    pass


class Problem(ProblemBase):
    pass