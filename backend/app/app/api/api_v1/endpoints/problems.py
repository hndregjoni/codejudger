from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session


from app import crud, models, schemas

# from app.models.problem import Problem
# from app.schemas.problem import ProblemCreate, ProblemUpdate
# from app.schemas.problem import Problem as ProblemSchema

from app.api import deps
from app.exceptions.tag import TagNotExistsError
from app.core.problem_manager import ProblemManager

router = APIRouter()

# Problems:
@router.get("/", response_model=List[schemas.Problem])
def get_problems(
    *,
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
    problem_manager: ProblemManager = Depends(deps.get_problem_manager)
) -> Any:
    """Get problems"""
    return crud.problem.get_problems_for_user(db, user_id=current_user.id, skip=skip, limit=limit)


@router.post("/")
def create_problem(
    *,
    db: Session = Depends(deps.get_db),
    problem_in: schemas.ProblemCreate,
    current_user: models.User = Depends(deps.get_current_active_user)
) -> Any:
    """ Creating a problem """

    try:
        item = crud.problem.create_problem(db, obj_in=problem_in, author_id=current_user.id)
        return item
    except TagNotExistsError as e:
        raise HTTPException(status_code=400, detail=f"The tag {e.tag} does not exist!")


@router.get("/id/{id}")
def get_problem_by_id(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user)
) -> Any:
    """ Get a problem by id. """
    problem = crud.problem.get(db, id=id)

    if not problem:
        raise HTTPException(status_code=404, detail=f"Problem not found")
    
    return problem


@router.get("/slug/{slug}")
def get_problem_by_slug(
    *,
    db: Session = Depends(deps.get_db),
    slug: str,
) -> Any:
    """ Get a problem by slug """
    problem = crud.problem.get_with_slug(db, slug=slug)

    if not problem:
        raise HTTPException(status_code=404, detail=f"Problem not found")
    
    return problem


# Problem statement

@router.get("/slug/{id}/statement", response_model=schemas.ProblemStatement)
def get_statement_by_id(
    *,
    db: Session = Depends(deps.get_db),
    id: int
) -> Any:
    """ Get the statement of a problem by its id """
    problem = crud.problem.get(db, id=id)

    if not problem:
        raise HTTPException(status_code=404, detail=f"Problem not found")

    return schemas.ProblemStatement(statement=problem.description)

@router.get("/slug/{slug}/statement", response_model=schemas.ProblemStatement)
def get_statement_by_slug(
    *,
    db: Session = Depends(deps.get_db),
    slug: str
) -> Any:
    """ Get the statement of a problem by its slug """
    problem = crud.problem.get_with_slug(db, slug=slug)

    if not problem:
        raise HTTPException(status_code=404, detail=f"Problem not found")

    return schemas.ProblemStatement(statement=problem.description)


# Testcases:

@router.get("/id/{id}/cases")
def get_testcases_by_id(
    *,
    db: Session = Depends(deps.get_db),
    id: int
) -> Any:
    """ Get the statement of a problem by its id """
    problem = crud.problem.get(db, id=id)

    if not problem:
        raise HTTPException(status_code=404, detail=f"Problem not found")
    
    pass


@router.get("/slug/{slug}/cases")
def get_testcases_by_slug(
    *,
    db: Session = Depends(deps.get_db),
    slug: str
) -> Any:
    """ Get the statement of a problem by its slug """
    problem = crud.problem.get_with_slug(db, slug=slug)

    if not problem:
        raise HTTPException(status_code=404, detail=f"Problem not found")

    pass


# Submissions:

@router.get("/id/{id}/subs")
def get_submissions_by_id(
    *,
    db: Session = Depends(deps.get_db),
    id: int, 
    current_user: models.User = Depends(deps.get_current_active_user)
) -> Any:
    """ Attempt a problem by id """
    pass


@router.get("/id/{slug}/subs")
def get_submissions_by_slug(
    *,
    db: Session = Depends(deps.get_db),
    slug: str, 
    current_user: models.User = Depends(deps.get_current_active_user)
) -> Any:
    """ Attempt a problem by id """
    pass