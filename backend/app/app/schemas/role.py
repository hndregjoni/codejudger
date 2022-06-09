from pydantic import BaseModel

extract_role_name = lambda role: role.role_name

class UserRole(BaseModel):
    id: int
    role_name: str

    class Config:
        orm_mode = True


class UserRoleCreate(UserRole):
    pass

class UserRoleUpdate(BaseModel):
    pass