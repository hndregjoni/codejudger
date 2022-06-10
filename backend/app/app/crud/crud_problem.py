from typing import List, Optional

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.crud import crud_tag
from app.models.problem import Problem
from app.schemas.problem import ProblemCreate, ProblemUpdate

class CRUDProblem(CRUDBase[Problem, ProblemCreate, ProblemUpdate]):
    def create_problem(
        self, db: Session, *, obj_in: ProblemCreate, author_id: int
    ) -> Problem:
        """
        Create a single problem, authored by author_id.
        """
        db_problem = Problem(
            slug=obj_in.slug,
            title=obj_in.title,
            description=obj_in.description
        )

        tags = crud_tag.tag.get_multi_poly(db, obj_in.tags)

        db_problem.tags.extend(tags)

        db.add(db_problem)
        db.commit()
        db.refresh(db_problem)

        # Do some magic here with respect to fs:

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