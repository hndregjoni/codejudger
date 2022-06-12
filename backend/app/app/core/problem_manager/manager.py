from .fs import ProblemFSManager
from .git import ProblemGitManager

class ProblemManager:
    problem_dir: str

    fs: ProblemFSManager
    git: ProblemGitManager

    def __init__(self, problem_dir):
        self.problem_dir = problem_dir

        self.fs = ProblemFSManager(problem_dir)
        self.git = ProblemGitManager(problem_dir)