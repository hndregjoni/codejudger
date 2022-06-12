from typing import Optional, List, Callable, Any

from yaml import dump

from os.path import (
    exists,
    join,
    isdir,
    islink
)

from os import mkdir,listdir,rename
import shutil

from .problem_manifest import ProblemManifest

class ProblemFSManager:
    problems_dir: str
    problem_manager: 'manager.ProblemManager'

    def __init__(self, problems_dir: str, problems_cache_dir: str, problem_manager: 'manager.ProblemManager'):
        self.problems_dir = problems_dir
        self.problems_cache_dir = problems_cache_dir

        self.problem_manager = problem_manager


    def _path(self, *p: List[str]) -> str:
        """ A path joining utility """
        return join(self.problems_dir, *p)
    
    def _path_c(self, *p: List[str]) -> str:
        """ A path joining utility for the cache"""
        return join(self.problems_cache_dir, *p)
 
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

        mpath = self._path(problem_slug, "problem.yml")

        ProblemManifest.parse_file(mpath)

    def write_manifest(self, problem_slug: str, manifest: ProblemManifest):
        """ Writes the given manifest. Overrides the one present. """        
        mpath = self._path(problem_slug, "problem.yml")

        with open(mpath, "w") as f:
            dump(manifest, f)
    
    def write_readme(self, problem_slug: str, description: str) -> None:
        rpath = self._path(problem_slug, "README.md")

        with open(rpath, "w") as f:
            f.write(description)
    
    def compress_problem(self, problem_slug: str, hash: str, format: str = "gztar", out_file: Optional[str] = None) -> str:
        """ Compress the given problem.
        
        Args:
            problem_slug:    The slug id of the problem
            format:          The archiving format, as per :func:`shutil.make_archive`
            out_file:        The archive without the format, as per :func:`shutil.make_archive`. 
              If None, one will be created in the problems cache directory, containing the hash in the name.

        """
        p = self._path(problem_slug)
        o = out_file or self._path_c(f"{problem_slug}_{hash}")

        if not exists(o):
            name = shutil.make_archive(out_file, o)
            rename(name, o)

        return o

from . import manager