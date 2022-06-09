from typing import Optional

from pydantic import BaseModel, constr

extract_slug = lambda tag: tag.slug

class TagBase(BaseModel):
    slug: constr(
        max_length=60,
        regex='^[a-zA-Z0-9_\-]*$')

    title: str

class TagWithIds(BaseModel):
    id: int 

    created_by_id: Optional[int]

    class Config:
        orm_mode = True

class Tag(TagBase, TagWithIds):
    pass

    class Config:
        orm_mode = True

class TagCreate(TagBase):
    pass

class TagUpdate(BaseModel):
    title: str