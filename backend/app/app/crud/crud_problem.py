from typing import List, Optional, Tuple
from datetime import datetime

from fastapi.encoders import jsonable_encoder
from sqlalchemy import not_
from sqlalchemy.orm import Session

from app import schemas, crud
from app.crud.base import CRUDBase, not_disabled_func
from app.models import User
from app.models.role import UserRoles
from app.models.problem import Problem
from app.schemas.problem import ProblemCreate, ProblemUpdate, TestCase
import app.core.problem_manager as problem_manager
from app.core.problem_manager.problem_manifest import ProblemManifest
from app.core.problem_manager.manager import ProblemManager
from app.models.submission import Submission
from app.schemas.attempt import SubmissionCreate
from app.models.attempt import ProblemAttempt

class CRUDProblem(CRUDBase[Problem, ProblemCreate, ProblemUpdate]):
    def create_problem(
        self,
        db: Session, 
        pm: problem_manager.ProblemManager,
        *,
        obj_in: ProblemCreate,
        author: User
    ) -> Problem:
        """
        Create a single problem, authored by author_id.
        """
        db_problem = Problem(
            slug=obj_in.slug,
            title=obj_in.title,
            description=obj_in.description,
            author_id=author.id
        )

        tags = crud.tag.get_multi_poly(db, obj_in.tags)
        db_problem.tags.extend(tags)

        # A way to determine the timespace constraints, for the given problem:
        # We have :
        # - Those specified in the contest it's attached to.
        # - Those specified in itself.
        # - Those global pertaining to each language (these could be cached, and can be redundant)

        # For now, some dummy values.
        spacetime = [schemas.SpaceTimeConstraint(
            time=2,
            space=2
        )]

        manifest = pm.build_manifest(obj_in, spacetime)
        # Create the directory (may throw an exception)
        pm.fs.create_directory(obj_in.slug)
        # Write the manifest file
        pm.fs.write_manifest(problem_slug=obj_in.slug, manifest=manifest)
        # Write the readme file:
        pm.fs.write_readme(problem_slug=obj_in.slug, description=obj_in.description)
        # Initialize and commit repo
        repo = pm.git.initialize_repo(obj_in.slug)
        # Commit repo
        hash = pm.git.commit_changes(author.username, repo=repo)
        # Save the hash in the model
        db_problem.head_commit = hash

        #TODO: handle a failure, cleanup the directory


        db.add(db_problem)
        db.commit()
        db.refresh(db_problem)

        return db_problem
    
    def can_be_attempted(
        self,
        db: Optional[Session],
        problem: Problem,
        moment: datetime = datetime.now()
    ) -> bool:
        """ Can a problem be solved right now, regardless of user? """
        pass
    
    def can_attempt(
        self,
        db: Session,
        user: User,
        problem: Problem,
        moment: datetime = datetime.now()
    ) -> bool:
        """ Can a user attempt a specific problem ? (Not disallowed by the constraintset) """
        return True
    
    def get_cases(
        self,
        db: Session, pm: ProblemManager,
        problem: Problem,
        manifest: ProblemManifest,
        filtered: bool = True
    ) -> List[TestCase]:
        manifest = pm.fs.read_manifest(problem.slug)
        
        cases = manifest.test.cases
        if filtered:
            cases = [case for case in cases if case.v]
        
        return cases
    
    def can_access(self, user: Optional[User], problem: Optional[Problem]) -> bool:
        """ Can a user access a problem ?"""
        # If no user, then whether not disabled:
        if not user:
            return not problem.disabled

        # If admin, then yes
        if crud.user.has_role(None, user, UserRoles.Admin):
            return True
        
        # Either user is author, or the problem is not disabled
        return problem.author_id == user.id or \
            not problem.disabled

    def get_problems_for_user(
        self, db: Session, *, user_id: int, skip: int = 0, limit: int = 10, listed: bool = True
    ) -> List[Problem]:
        """ Get the problems accessible by a user.

        This usually means:

        1. Publicly visible problems.
        2. Problems that are constrained to this user.
        
        """

        # For now, return all visible problems:

        query = self._base_query(db, True) \
            .filter(not_(Problem.disabled)) \
            .filter(Problem.listed == listed)

        paginated = self.paginate(
            query,
            skip=skip, limit=limit
        ).all()

        return paginated


    def get_with_slug(self, db: Session, slug: str) -> Optional[Problem]:
        """ Get an tag by its slug """
        return self.get_with_filter(db, self.model.slug == slug)
    
    def get_or_create_attempt(
        self,
        db: Session,
        user: User,
        problem: Problem
    ) -> Tuple[ProblemAttempt, bool]:
        """ Gets an attempt between user-problem, or creats one.
        
        Returns:
            (attempt, new): The attempt and whether it was newly created. """

        new = False
        attempt = db.query(ProblemAttempt).filter(
            ProblemAttempt.user_id == user.id,
            ProblemAttempt.problem_id == problem.id
        ).first()

        if not attempt:
            new = True
            new_attempt = ProblemAttempt()
            new_attempt.user_id = user.id
            new_attempt.problem_id = problem.id
            attempt = new_attempt
        
        return attempt, new

    def add_submission(
        self,
        db: Session,
        problem: Problem,
        user: User,
        obj_in: SubmissionCreate
    ) -> Tuple[Submission, ProblemAttempt]:
        """ Adds a submission between specified user and problem. """

        # First check whether an attempt between the two exists, if not
        # create one
        attempt, new = self.get_or_create_attempt(db, user, problem)

        obj_in_data = jsonable_encoder(obj_in)
        new_sub = Submission(**obj_in_data)
        new_sub.user_id = user.id
        new_sub.problem_id = problem.id

        if new:
            attempt.first_submission = new_sub 

        if new:
            db.add(attempt)
        
        db.add(new_sub)
        db.commit()
        db.refresh(new_sub)
        db.refresh(attempt)

        return new_sub, attempt


problem = CRUDProblem(Problem)