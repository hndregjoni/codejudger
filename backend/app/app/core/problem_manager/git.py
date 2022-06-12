from typing import Optional

import git
from git.repo.base import Repo

from git import Repo

class ProblemGitManager:
    """ The class responsible for managing the git repo of a problem. 
    A composite item of a :class:`.manager.ProblemManager`

    Attributes:
        problem_dir     The directory storing all the problems.
        problem_manager A reference to the containing problem manager
    """
    problem_dir: str
    problem_manager: 'manager.ProblemManager'

    SOUGHT_FILES=['problem.yml', 'README.md']

    def __init__(self, problem_dir: str, problem_manager: 'manager.ProblemManager'):
        self.problem_dir = problem_dir
        self.problem_manager = problem_manager
    
    def check_repo(self, problem_slug: str) -> bool:
        """ Check whether the given problem_slug has an initialized repo """
        p = self.problem_manager.fs._path(problem_slug)

        try:
            _ = git.Repo(p).git_dir
            return True
        except git.exc.InvalidGitRepositoryError:
            return False
    
    def git_repo(self, problem_slug: str) -> Optional[Repo]:
        """ Check whether the given problem directory is an actual git repository """

        p = self.problem_manager.fs._path(problem_slug)
        return git.Repo(p).git_dir

    def get_head_commit(self, problem_slug: str = None, repo: Repo = None) -> str:
        """ Returns a commit hash of the HEAD of the repository. """
        repo = repo or self.git_repo(problem_slug)

        hexsha = repo.head.commit.hexsha
        short_sha = repo.git.rev_parse(hexsha, short=6)

        return short_sha
    
    def initialize_repo(self, problem_slug: str) -> Repo:
        """ Initialize a given problem with a repository """
        p = self.problem_manager.fs._path(problem_slug)
        return git.Repo.init(p)

    def commit_changes(self, problem_slug: str) -> bool:
        """ Commit the changes of the conventional files and returns the new hash """ 
        repo = repo or self.git_repo(problem_slug)

        repo.add(self.SOUGHT_FILES)
        repo.commit()

        return self.get_head_commit(repo=repo)

    def git_clone(self, problem_slug_in: str, problem_slug_out: str):
        """ Clone the given problem_slug_in into the problem_slug_out """
        pass
    
    def git_clone_repote(self, problem_slug: str, url: str):
        """ Clone remote repository """
        pass

from . import manager