from typing import Any, Dict, Optional, Union

from sqlalchemy import or_
from sqlalchemy.orm import Session

from app import crud
from app.core.security import get_password_hash, verify_password
from app.crud.base import CRUDBase
from app.models.user import User, user_roles
from app.models.role import UserRole, UserRoles
from app.schemas.user import UserCreate, UserUpdate


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    def get_by_email(self, db: Session, *, email: str) -> Optional[User]:
        return db.query(User).filter(User.email == email).first()

    def get_by_username(self, db: Session, *, username: str) -> Optional[User]:
        return db.query(User).filter(User.username == username).first()
    
    def get_by_username_or_email(
        self,
        db: Session,
        *,
        username: str,
        email: str
    ) -> Optional[User]:
        return db.query(User).filter(or_(User.username == username, User.email == email)).first()

    def create(self, db: Session, *, obj_in: UserCreate, is_active: bool = False) -> User:
        db_obj = User(
            username=obj_in.username,
            email=obj_in.email,
            hashed_password=get_password_hash(obj_in.password),
            full_name=obj_in.full_name,
            is_active=False
        )

        db_obj.roles = []

        tags = crud.tag.get_multi_poly(db, obj_in.interests)
        db_obj.interests.extend(tags)

        self.assign_role(db, db_obj, UserRoles.Solver, commit=False)

        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, *, db_obj: User, obj_in: Union[UserUpdate, Dict[str, Any]]
    ) -> User:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        if update_data["password"]:
            hashed_password = get_password_hash(update_data["password"])
            del update_data["password"]
            update_data["hashed_password"] = hashed_password
        return super().update(db, db_obj=db_obj, obj_in=update_data)

    def authenticate(self, db: Session, *, identifier: str, password: str) -> Optional[User]:
        user = self.get_by_username_or_email(db, username=identifier, email=identifier)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user

    def is_active(self, user: User) -> bool:
        return user.is_active

    def is_superuser(self, user: User) -> bool:
        return user.is_superuser
    
    def assign_role(self, db: Session, user: User, role: UserRoles, commit: bool = True) -> bool:
        """ Assing the roles, and return whether the assignment was effective """ 
        if self.has_role(db, user, role):
            return False
        
        role = db.query(UserRole).filter(UserRole.id == role.value).first()

        user.roles.append(role)
        if commit:
            db.commit()
        return True


    def has_role(self, db: Session, user: User, role: UserRoles) -> bool:
        """
        Does the user have the role ?
        """ 

        return any([u_role.id == role.value for u_role in user.roles])
    
    def activate_user(self, db: Session, user: User) -> bool:
        """ Activate a user """
        if user.activated_once == False:
            user.activated_once = True
        
        user.is_active = True
        db.commit()

        return user.is_active

    
    def deactivate_user(self, db: Session, user: User) -> bool:
        """ Deactivate a user """ 
        user.is_active = False
        db.commit()

        return user.is_active

user = CRUDUser(User)
