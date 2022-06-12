from typing import List, Optional

from dataclasses import dataclass
from pydantic import BaseModel
from pydantic_yaml import YamlModelMixin

from app import schemas

@dataclass
class ProblemDescription:
    file: Optional[str]
    text: Optional[str]

class ProblemTestCase(schemas.TestCase):
    pass

@dataclass
class ProblemTest:
    cases: List[ProblemTestCase]

class SpaceTimeConstraint(YamlModelMixin, schemas.SpaceTimeConstraint):
    pass

class ProblemManifest(YamlModelMixin, BaseModel):
    version: float

    description: ProblemDescription
    constraints: List[SpaceTimeConstraint] = []

    test: ProblemTest