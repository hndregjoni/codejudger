from typing import List

from dataclasses import dataclass
from pydantic import BaseModel
from pydantic_yaml import YamlModelMixin

from app.schemas.problem import TestCase

@dataclass
class ProblemDescription:
    file: str
    text: str

class ProblemTestCase(TestCase):
    pass

@dataclass
class ProblemTest:
    cases: List[ProblemTestCase]

@dataclass
class ProblemConstraints:
    time: int
    space: int

class ProblemManifest(YamlModelMixin, BaseModel):
    version: float

    description: ProblemDescription
    constraints: ProblemConstraints

    test: ProblemTest