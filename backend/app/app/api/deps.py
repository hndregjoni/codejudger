from typing import Generator, Callable, Optional

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from pydantic import ValidationError
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.core import security
from app.core.config import settings
from app.db.session import SessionLocal
from app.core.problem_manager import ProblemManager
from app.exceptions.http.auth import UserInactiveError

reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR}/auth/login"
)

reusable_oauth2_noerr = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR}/auth/login",
    auto_error=False
)


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def _get_user(
    token_dep, required: bool
):
    def get_user(
        db: Session = Depends(get_db), token: str = Depends(token_dep)
    ) -> Optional[models.User]:
        if not required and not token:
            # Token is not required, so we return None
            return None
        try:
            payload = jwt.decode(
                token, settings.SECRET_KEY, algorithms=[security.ALGORITHM]
            )
            token_data = schemas.TokenPayload(**payload)
        except (jwt.JWTError, ValidationError):
            # If token was sepcified, we always check it
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Could not validate credentials",
            )

        # Again, there was a token, it requirested a user, so we check it 
        user = crud.user.get(db, id=token_data.sub)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user
    
    return get_user


def _filter_active(get_user_dep):
    def filter_active(user = Depends(get_user_dep)):
        if not crud.user.is_active(user):
            raise UserInactiveError(user.username)
        
        return user
    
    return filter_active


def make_user_dependency(required: bool = True, only_active: bool = True):

    get_user = _get_user(
        token_dep=reusable_oauth2 if required else reusable_oauth2_noerr,
        required=required
    )

    if only_active:
        # Apply one extra level
        get_user = _filter_active(get_user)
    
    # Here we do the scoping authorization thing:
    # TODO

    return get_user


get_current_user = make_user_dependency(required=True, only_active=False)
get_current_active_user = make_user_dependency(required=True, only_active=True)


def get_problem_manager() -> ProblemManager:
    return ProblemManager(settings.PROBLEMS_DIR, settings.PROBLEMS_CACHE)