from typing import Any, List, Optional

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps
from app.core.config import settings
from app.utils import send_new_account_email
from app.exceptions.http.auth import NoOpenUserRegistrationError
from app.exceptions.http.user import UserExistsError
from app.exceptions.tag import TagNotFoundException
from app.exceptions.http.tag import TagNotFoundError

router = APIRouter()


@router.get("/", response_model=List[schemas.User])
def read_users(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve users.
    """
    users = crud.user.get_multi(db, skip=skip, limit=limit)
    return users


@router.post("/", response_model=schemas.User)
def create_user(
    *,
    db: Session = Depends(deps.get_db),
    user_in: schemas.UserCreate,
    current_user: Optional[models.User] = Depends(deps.make_user_dependency(
        required=False, # Open login
        only_active=True # If not opne, we need an active superuser
        # TODO: admin scope here
    ))
) -> Any:
    """
    Create new user.
    """

    if not current_user and not settings.USERS_OPEN_REGISTRATION:
        raise NoOpenUserRegistrationError()

    user = crud.user.get_by_username_or_email(db, username=user_in.username, email=user_in.email)

    if user:
        raise UserExistsError(user.username)
    
    try:
        user = crud.user.create(db, obj_in=user_in)
    except TagNotFoundException as e:
        raise TagNotFoundError(e.tag)

    if settings.EMAILS_ENABLED and user_in.email:
        send_new_account_email(
            email_to=user_in.email, username=user_in.email, password=user_in.password
        )

    return user


@router.put("/me", response_model=schemas.User)
def update_user_me(
    *,
    db: Session = Depends(deps.get_db),
    password: str = Body(None),
    full_name: str = Body(None),
    email: EmailStr = Body(None),
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update own user.
    """
    current_user_data = jsonable_encoder(current_user)
    user_in = schemas.UserUpdate(**current_user_data)
    if password is not None:
        user_in.password = password
    if full_name is not None:
        user_in.full_name = full_name
    if email is not None:
        user_in.email = email
    user = crud.user.update(db, db_obj=current_user, obj_in=user_in)
    return user


@router.get("/me", response_model=schemas.User)
def read_user_me(
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get current user.
    """
    return current_user

@router.get("/id/{user_id}", response_model=schemas.User)
def read_user_by_id(
    user_id: int,
    current_user: models.User = Depends(deps.get_current_active_user), #TODO: super
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Get a specific user by id.
    """
    user = crud.user.get(db, id=user_id)
    if user == current_user:
        return user
    if not crud.user.is_superuser(current_user):
        raise HTTPException(
            status_code=400, detail="The user doesn't have enough privileges"
        )
    return user

@router.get("/id/{user_id}/active")
def get_active_status(
    user_id: int,
    db: Session = Depends(deps.get_db)
) -> Any:
    """ Get user active status """

@router.put("/id/{user_id}/active")
def activate_user(
    user_id: int,
    db: Session = Depends(deps.get_db),
    user: models.User = Depends(deps.get_current_active_user) #TODO: super
) -> Any:
    """ Activate the user """

@router.delete("/id/{user_id}/active")
def deactivate_user(
    user_id: int,
    db: Session = Depends(deps.get_db),
    user: models.User = Depends(deps.get_current_active_user) #TODO: super
) -> Any:
    """ Deactivate user"""


@router.get("/id/{user_id}/social")
def get_user_social_by_id(
    user_id: int,
    db: Session = Depends(deps.get_db)
) -> Any:
    """ Get a user's social info """

@router.get("/id/{user_id}/followers")
def get_user_followers(
    user_id: int,
    db: Session = Depends(deps.get_db)
) -> Any:
    """ Get user followers """

@router.get("/id/{user_id}/following")
def get_user_following(
    user_id: int,
    db: Session = Depends(deps.get_db)
) -> Any:
    """ Get user following """

@router.get("/id/{user_id}/follow")
def get_brief_follow_count(
    user_id: int,
    db: Session = Depends(deps.get_db)
) -> Any:
    """ Get a brief follow information over this user """

@router.put("/id/{user_id}/follow")
def follow_user(
    user_id: int,
    active_user: models.User = Depends(deps.get_current_active_user),
    db: Session = Depends(deps.get_db)
) -> Any:
    """ Follow this user """

@router.delete("/id/{user_id}/follow")
def unfollow_user(
    user_id: int,
    active_user: models.User = Depends(deps.get_current_active_user),
    db: Session = Depends(deps.get_db)
) -> Any:
    """ Unfollow this user """

@router.put("/id/{user_id}", response_model=schemas.User)
def update_user(
    *,
    db: Session = Depends(deps.get_db),
    user_id: int,
    user_in: schemas.UserUpdate,
    current_user: models.User = Depends(deps.get_current_active_user), #TODO: super
) -> Any:
    """
    Update a user.
    """
    user = crud.user.get(db, id=user_id)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="The user with this username does not exist in the system",
        )
    user = crud.user.update(db, db_obj=user, obj_in=user_in)
    return user
