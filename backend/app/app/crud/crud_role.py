from typing import Optional

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.role import UserRole
from app.schemas.role import UserRoleCreate, UserRoleUpdate
from app.schemas.role import UserRole as UserRoleSchema

class CRUDRole(CRUDBase[UserRoleSchema, UserRoleCreate, UserRoleUpdate]):
    def get_by_rolename(self, db: Session, role_name: str):
        return self.get_with_filter(db, self.model.rolen_name == role_name)


role = CRUDRole(UserRole)