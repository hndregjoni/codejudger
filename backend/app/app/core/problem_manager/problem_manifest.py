from typing import List, Optional

from collections import OrderedDict

from pydantic import BaseModel

import yaml

from app import schemas

class ProblemDescription(BaseModel):
    file: Optional[str]
    text: Optional[str]

class ProblemTestCase(schemas.TestCase):
    pass

class ProblemTest(BaseModel):
    cases: List[ProblemTestCase]

class SpaceTimeConstraint(schemas.SpaceTimeConstraint):
    pass

class ProblemManifest(BaseModel):
    version: float

    description: ProblemDescription
    constraints: List[SpaceTimeConstraint] = []

    test: ProblemTest

def dump_yaml(manifest: ProblemManifest, f):
    """ Build a yaml manually"""
    obj = OrderedDict()

    obj['version'] = manifest.version
    obj['description'] = {
        'file': manifest.description.file,
        'text': manifest.description.text
    }

    obj['constraints'] = [c.dict() for c in manifest.constraints]

    obj['test'] = {
        'cases': [case.dict() for case in manifest.test.cases]
    }

    yaml.dump(obj, f)


def read_yaml(input: str) -> ProblemManifest:
    """ Decode the YAML """
    a = yaml.safe_load(input)
    return ProblemManifest(**a)