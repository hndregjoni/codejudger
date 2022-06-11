class ProblemGitManager:
    problem_dir: str

    def __init__(self, problem_dir: str):
        self.problem_dir = problem_dir
    
    def check_git_repo(self, problem_slug: str) -> bool:
        """ Check whether the given problem directory is an actual git repository """
        pass

    def get_head_commit(self, problem_slug: str) -> str:
        """ Returns a commit hash of the HEAD of the repository. """
        pass

    def commit_changes(self, problem_slug: str) -> bool:
        """ Commit the changes of the conventional files. """
        pass