from typing import Any, List

from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_submissions() -> Any:
    """ Get submissions"""
    return []