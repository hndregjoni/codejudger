from sqlalchemy.orm import Session

from app import crud, schemas, models
from app.core.config import settings
from app.db import base  # noqa: F401

def init_roles(db: Session) -> None:
    """ Initialize the roles of the system, from te enum. """

    print("Here")
    for enum_role in models.role.UserRoles: 
        role_name, role_id = enum_role.name, enum_role.value

        role = crud.role.get(db, role_id)        

        if not role:
            role_in = schemas.UserRoleCreate(
                id = role_id,
                role_name = role_name
            )

            role = crud.role.create(db, obj_in=role_in)

def init_db(db: Session) -> None:
    """ Seed the initial system data """
    init_roles(db)

    user = crud.user.get_by_username_or_email(db, username=settings.FIRST_SUPERUSER_USERNAME, email=settings.FIRST_SUPERUSER_EMAIL)
    if not user:
        user_in = schemas.UserCreate(
            username=settings.FIRST_SUPERUSER_USERNAME,
            email=settings.FIRST_SUPERUSER_EMAIL,
            password=settings.FIRST_SUPERUSER_PASSWORD,
            is_superuser=True,
        )
        user = crud.user.create(db, obj_in=user_in, is_active=True)  # noqa: F841

        crud.user.assign_role(db, user, models.role.UserRoles.Admin)
        crud.user.assign_role(db, user, models.role.UserRoles.Solver)
        crud.user.assign_role(db, user, models.role.UserRoles.Setter)