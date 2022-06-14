from typing import Generic, TypeVar, Type, Optional, Any, Union, List

from dataclasses import dataclass
from pydantic import BaseModel
from fastapi import Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse


InnerT = TypeVar('InnerT')
ErrorT = TypeVar("ErrorT", bound='BaseError[Any]')

def removesuffix(string: str, suffix: str):
    if string.endswith(suffix):
        return string[:-len(suffix)]
    
    return string

class Model(BaseModel):
    code: Optional[int]
    message: Optional[str]
    payload: Optional[Union[str, List[str]]]
    type: str

class Wrapper(BaseModel):
    detail: Model

Payload = Optional[Union[str, List[str]]]

@dataclass
class BaseError(Exception):

    model: 'BaseError.Model'
    CODE: int = 400

    def __init__(self, error_type: type, payload: Payload = None, message: str = None, code: Optional[int] = None):
        super(Exception, self).__init__(message)

        self.model = Model(
            message=message,
            payload=payload,
            type=removesuffix(error_type.__name__, "Error"),
            code = code or self.CODE
        )
    
    def wrapped_dict(self: ErrorT) -> Any:
        return (Wrapper(detail=self.model).dict())
    
    @classmethod
    def responses(cls):
        return {
            BaseError.CODE: {"model": Wrapper}
        }

async def handle_base_error(request: Request, exc: BaseError):
    return JSONResponse(exc.wrapped_dict(), status_code=exc.model.code)