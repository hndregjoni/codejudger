from typing import List, Optional

import app.schemas as schemas
from app.schemas import ProblemCreate

from app.core.problem_manager.problem_manifest import (
    ProblemManifest, ProblemTest, ProblemDescription
)


# Here for now (or -ever)
MANIFEST_VERSION=1.0

class ProblemManager:
    problems_dir: str
    problems_cache_dir: str

    fs: 'ProblemFSManager'
    git: 'ProblemGitManager'

    def __init__(self, problems_dir: str, problems_cache_dir: str):
        self.problems_dir = problems_dir
        self.problems_cache_dir = problems_cache_dir

        self.fs = ProblemFSManager(problems_dir, problems_cache_dir, self)
        self.git = ProblemGitManager(problems_dir, problems_cache_dir, self)
    
    def build_manifest(
        self,
        problem_in: ProblemCreate,
        constraints: Optional[List[schemas.SpaceTimeConstraint]]
    ) -> ProblemManifest:
        """ Givn the problem schema, build the manifest schema """

        result = ProblemManifest(
            version=MANIFEST_VERSION,
            description=ProblemDescription(
                file="README.md",
                text=None
            ),

            constraints=constraints or [],

            test=ProblemTest(
                cases=problem_in.test_cases 
            )
        )

        return result

from .fs import ProblemFSManager
from .git import ProblemGitManager