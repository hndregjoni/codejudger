from typing import Optional

from .problem_manifest import ProblemManifest

class ProblemFSManager:
    problem_dir: str

    def __init__(self, problem_dir: str):
        self.problem_dir = problem_dir
        pass
    
    def check_exists(self, problem_slug: str) -> bool:
        """ Check if problem already exists in directory """
        pass
    
    def create_directory(self, problem_slug: str) -> bool:
        """ Create a problem directory """
        pass

    def check_not_empty(self, problem_slug: str) -> bool:
        """ Check whether the given problem has any files in it """
        pass
    
    def check_valid_structure(self, problem_slug: str) -> bool:
        """ Check whether the given problem has a proper directory structure """
        pass

    def check_soft_link(self, problem_slug: str) -> Optional[str]:
        """ Check whether the given problem is soft linked """
        pass
    
    def read_manifest(self, problem_slug: str) -> ProblemManifest:
        """ Reads the manifest from the problem directory """
        pass

    def write_manifest(self, problem_slug: str, manifest: ProblemManifest):
        """ Writes the given manifest. Overrides the one present. """
        pass