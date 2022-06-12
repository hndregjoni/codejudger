from typing import List, Optional

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app import schemas
from app.crud.base import CRUDBase
from app.crud import crud_tag
from app.models import User
from app.models.problem import Problem
from app.schemas.problem import ProblemCreate, ProblemUpdate
import app.core.problem_manager as problem_manager

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

        tags = crud_tag.tag.get_multi_poly(db, obj_in.tags)
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


    def get_problems_for_user(
        self, db: Session, *, user_id: int, skip: int = 0, limit: int = 10
    ) -> List[Problem]:
        """ Get the problems accessible by a user.

        This usually means:

        1. Publicly visible problems.
        2. Problems that are constrained to this user.
        
        """

        # For now, return all visible problems:
        return self.paginate(
            db.query(self.model)

            , skip=skip, limit=limit
        ).all()

    def get_with_slug(self, db: Session, slug: str) -> Optional[Problem]:
        """ Get an tag by its slug """
        return self.get_with_filter(db, self.model.slug == slug)

problem = CRUDProblem(Problem)