from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.problem import Problem
from app.schemas.problem import ProblemCreate, ProblemUpdate

class CRUDProblem(CRUDBase[Problem, ProblemCreate, ProblemUpdate]):
    def create_problem(
        self, db: Session, *, obj_in: ProblemCreate, author_id: int, skip
    ) -> Problem:
        """ Create a single problem, authored by author_id.
        """
        pass

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


problem = CRUDProblem(Problem)