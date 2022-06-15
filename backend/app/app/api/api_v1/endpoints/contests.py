from typing import Any, List

from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_contests() -> Any:
    """ Get contests"""
    return []

@router.post("/")
def create_contest() -> Any:
    """ Create a contest """

@router.get("/id/{id}")
def get_contest_by_id(id: int) -> Any:
    """ Get a contest by its id """

@router.get("/slug/{slug}")
def get_contest_with_slug(slug: str) -> Any:
    """ Get a contest by its slug """

@router.get("/id/{id}/problems")
def get_contest_problems_by_id(id: int) -> Any:
    """ Get a contest's problems by its id"""
    pass

@router.get("/slug/{slug}/problems")
def get_contest_problems_by_id(slug: str) -> Any:
    """ Get a contest's problems by its id"""
    pass

@router.get("/id/{id}/standings")
def get_contest_standings_by_id(id: int) -> Any:
    """ Get a contest's standings by its id """

@router.get("/slug/{slug}/standings")
def get_contest_standings_by_id(slug: str) -> Any:
    """ Get a contest's standings by its slug """