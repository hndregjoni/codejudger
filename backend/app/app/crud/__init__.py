from .crud_item import item
from .crud_user import user
from .crud_problem import problem
from .crud_language import language
from .crud_tag import tag
from .crud_role import role

# For a new basic set of CRUD operations you could just do

# from .base import CRUDBase
# from app.models.item import Item
# from app.schemas.item import ItemCreate, ItemUpdate

# item = CRUDBase[Item, ItemCreate, ItemUpdate](Item)
