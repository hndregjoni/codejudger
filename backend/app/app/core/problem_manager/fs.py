from typing import Optional, List, Callable, Any

from yaml import dump

from os.path import (
    exists,
    join,
    isdir,
    islink
)

from os import mkdir,listdir

from .problem_manifest import ProblemManifest

class ProblemFSManager:
    problem_dir: str
    problem_manager: 'manager.ProblemManager'

    def __init__(self, problem_dir: str, problem_manager: 'manager.ProblemManager'):
        self.problem_dir = problem_dir
        self.problem_manager = problem_manager


    def _path(self, *p: List[str]):
        return join(self.dir, *p)
 
    def check_exists(self, problem_slug: str) -> bool:
        """ Checks whether directory exists """
        p = self._path(problem_slug)
        return exists(p) and isdir(p)
    
    def create_directory(self, problem_slug: str) -> None:
        """ Create a problem directory """
        new_p = self._path(problem_slug)
        mkdir(new_p)
    
    def dir_entries(self, problem_slug: str) -> List[str]:
        """ Get the entries of the directory """
        p = self._path(problem_slug)
        return listdir(p)

    def check_not_empty(self, problem_slug: str) -> bool:
        """ Check whether the given problem has any files in it """
        return len(self.dir_entries(problem_slug)) > 0
    
    def check_valid_structure(self, problem_slug: str) -> bool:
        """ Check whether the given problem has a proper directory structure """

        dir_entries = self.dir_entries(problem_slug)

        return all(
            'problem.yml' in dir_entries,
            'README.md' in dir_entries
        )

    def check_link(self, problem_slug: str) -> Optional[str]:
        """ Check whether the given problem is soft linked """
        p = self._path(problem_slug)

        return islink(p)
    
    def read_manifest(self, problem_slug: str) -> ProblemManifest:
        """ Reads the manifest from the problem directory """

        mpath = self._path(problem_slug, "manifest.yml")

        ProblemManifest.parse_file(mpath)

    def write_manifest(self, problem_slug: str, manifest: ProblemManifest):
        """ Writes the given manifest. Overrides the one present. """        
        mpath = self._path(problem_slug, "manifest.yml")

        with open(mpath, "w") as f:
            dump(manifest, f)

from . import manager