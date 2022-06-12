from .fs import ProblemFSManager
from .git import ProblemGitManager

class ProblemManager:
    problems_dir: str
    problems_cache_dir: str

    fs: ProblemFSManager
    git: ProblemGitManager

    def __init__(self, problems_dir: str, problems_cache_dir: str):
        self.problems_dir = problems_dir
        self.problems_cache_dir = problems_cache_dir

        self.fs = ProblemFSManager(problems_dir, problems_cache_dir, self)
        self.git = ProblemGitManager(problems_dir, problems_cache_dir, self)