from fastapi import APIRouter

from app.api.api_v1.endpoints import items, login, users, utils, problems, submissions, contests, languages, tags

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(utils.router, prefix="/utils", tags=["utils"])

api_router.include_router(problems.router, prefix="/problems", tags=["problems"])
api_router.include_router(submissions.router, prefix="/submissions", tags=["submissions"])
api_router.include_router(contests.router, prefix="/contests", tags=["contests"])
api_router.include_router(languages.router, prefix='/languages', tags=['languages'])
api_router.include_router(tags.router, prefix='/tags', tags=['tags'])
