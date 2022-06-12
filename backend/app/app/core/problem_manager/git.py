from typing import Optional

import git
from git.repo.base import Repo
from git.objects.commit import Commit

from git import Repo

class ProblemGitManager:
    """ The class responsible for managing the git repo of a problem. 
    A composite item of a :class:`.manager.ProblemManager`

    Attributes:
        problems_dir:        The directory storing all the problems
        problem_cache_dir:  The problem cache directory
        problem_manager:    A reference to the containing problem manager
    """
    problems_dir: str
    problems_cache_dir: str
    problem_manager: 'manager.ProblemManager'

    SOUGHT_FILES=['problem.yml', 'README.md']

    def __init__(self, problems_dir: str, problems_cache_dir: str, problem_manager: 'manager.ProblemManager'):
        self.problems_dir = problems_dir
        self.problems_cache_dir = problems_cache_dir
        
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

    def get_head_commit(self, problem_slug: str = None, repo: Repo = None, commit: Commit = None) -> str:
        """ Returns a commit hash of the HEAD of the repository. """
        repo = repo or self.git_repo(problem_slug)
        head_commit = commit or repo.head.commit

        hexsha = head_commit.hexsha
        short_sha = repo.git.rev_parse(hexsha, short=6)

        return short_sha
    
    def initialize_repo(self, problem_slug: str = None) -> Repo:
        """ Initialize a given problem with a repository """
        p = self.problem_manager.fs._path(problem_slug)
        return git.Repo.init(p)

    def commit_changes(self, author_name: str, problem_slug: str = None, repo: Repo = None) -> str:
        """ Commit the changes of the conventional files and returns the new hash """ 
        repo = repo or self.git_repo(problem_slug)

        repo.index.add(self.SOUGHT_FILES)
        c = repo.index.commit(f"Authored:{author_name}")

        return self.get_head_commit(repo=repo, commit=c)

    def git_clone(self, problem_slug_in: str, problem_slug_out: str):
        """ Clone the given problem_slug_in into the problem_slug_out """
        pass
    
    def git_clone_repote(self, problem_slug: str, url: str):
        """ Clone remote repository """
        pass

from . import manager