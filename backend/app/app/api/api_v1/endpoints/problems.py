from typing import Any, List, Optional

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import Response

from sqlalchemy.orm import Session


from app import crud, models, schemas

# from app.models.problem import Problem
# from app.schemas.problem import ProblemCreate, ProblemUpdate
# from app.schemas.problem import Problem as ProblemSchema

from app.api import deps
from app.exceptions.tag import TagNotExistsError
from app.core.problem_manager import ProblemManager
from app.exceptions.http.problem import ProblemNotFoundError

router = APIRouter()

# Util
def problem_hoops(
    problem: Optional[models.Problem],
    user: Optional[models.User],
    slug: Optional[str] = None,
    id: Optional[int] = None
):
    if not problem:
        raise ProblemNotFoundError(slug=slug, id=id)
        # raise HTTPException(status_code=404, detail=f"Problem not found")
    
    if not crud.problem.can_access(user, problem):
        raise HTTPException(status_code=400, detail="User cannot acces the problem")
    
    return problem

responses = {**ProblemNotFoundError.responses()}


# Problems:
@router.get("/", response_model=List[schemas.Problem])
def get_problems(
    *,
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user)
) -> Any:
    """Get problems"""
    return crud.problem.get_problems_for_user(db, user_id=current_user.id, skip=skip, limit=limit)


@router.post("/")
def create_problem(
    *,
    db: Session = Depends(deps.get_db),
    problem_in: schemas.ProblemCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
    pm: ProblemManager = Depends(deps.get_problem_manager)
) -> Any:
    """ Creating a problem """

    problem = crud.problem.get_with_slug(db, slug=problem_in.slug)

    if problem:
        raise HTTPException(status_code=400, detail=f"Problem with the same slug exists!")

    try:
        item = crud.problem.create_problem(db, pm, obj_in=problem_in, author=current_user)
        return item
    except TagNotExistsError as e:
        raise HTTPException(status_code=400, detail=f"The tag {e.tag} does not exist!")


@router.get("/id/{id}", responses=responses)
def get_problem_by_id(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user)
) -> Any:
    """ Get a problem by id. """
    problem = crud.problem.get(db, id=id)

    problem = problem_hoops(problem, current_user, id=id)

    return problem


@router.get("/slug/{slug}")
def get_problem_by_slug(
    *,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
    slug: str,
) -> Any:
    """ Get a problem by slug """
    problem = crud.problem.get_with_slug(db, slug=slug)

    problem = problem_hoops(problem, current_user, slug=slug)
    
    return problem


# Problem statement

@router.get("/id/{id}/statement", response_model=schemas.ProblemStatement)
def get_statement_by_id(
    *,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
    id: int
) -> Any:
    """ Get the statement of a problem by its id """
    problem = crud.problem.get(db, id=id)

    problem = problem_hoops(problem, current_user, id=id)

    return schemas.ProblemStatement(statement=problem.description)

@router.get("/slug/{slug}/statement", response_model=schemas.ProblemStatement)
def get_statement_by_slug(
    *,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
    slug: str
) -> Any:
    """ Get the statement of a problem by its slug """
    problem = crud.problem.get_with_slug(db, slug=slug)

    problem = problem_hoops(problem, current_user, slug=slug)

    return schemas.ProblemStatement(statement=problem.description)


# Manifest.yml
manifest_response = {
    200: {
        "content": {"text/yaml": {}},
        "description": "The problem manifest",
    }
}
@router.get(
    "/id/{id}/problem.yml",
    responses={**manifest_response})
def get_manifest_by_id(
    *,
    db: Session = Depends(deps.get_db),
    pm: ProblemManager = Depends(deps.get_problem_manager),
    id: int
) -> Any:
    """ Get problem manifest file by id """
    problem = crud.problem.get(db, id=id)

    problem = problem_hoops(problem, None, id=id)

    return Response(pm.fs.read_manifest_raw(problem.slug), media_type="text/yaml")

@router.get(
    "/slug/{slug}/problem.yml",
    responses={**manifest_response})
def get_manifest_by_slug(
    *,
    db: Session = Depends(deps.get_db),
    pm: ProblemManager = Depends(deps.get_problem_manager),
    slug: str
) -> Any:
    """ Get problem manifest file by slug """
    problem = crud.problem.get_with_slug(db, slug=slug)

    problem = problem_hoops(problem, None, slug=slug)

    return Response(pm.fs.read_manifest_raw(slug), media_type="text/yaml")


# Testcases:

@router.get("/id/{id}/cases", response_model=List[schemas.TestCase])
def get_testcases_by_id(
    *,
    db: Session = Depends(deps.get_db),
    pm: ProblemManager = Depends(deps.get_problem_manager),
    current_user: models.User = Depends(deps.get_current_active_user),
    id: int
) -> Any:
    """ Get the statement of a problem by its id """
    problem = crud.problem.get(db, id=id)

    problem = problem_hoops(problem, current_user, id=id)

    manifest = pm.fs.read_manifest(problem.slug)
    return manifest.test.cases


@router.get("/slug/{slug}/cases", response_model=List[schemas.TestCase])
def get_testcases_by_slug(
    *,
    db: Session = Depends(deps.get_db),
    pm: ProblemManager = Depends(deps.get_problem_manager),
    current_user: models.User = Depends(deps.get_current_active_user),
    slug: str
) -> Any:
    """ Get the statement of a problem by its slug """
    problem = crud.problem.get_with_slug(db, slug=slug)

    problem = problem_hoops(problem, current_user, slug=slug)

    manifest = pm.fs.read_manifest(problem.slug)
    return manifest.test.cases


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