from typing import Optional

from datetime import datetime
from pydantic import BaseModel, Field

from app.core.config import settings

class Submission(BaseModel):
    language_id: str

class SubmissionCreate(Submission):
    code: str = Field(..., max_length=settings.MAX_SOL_LEN)

class SubmissionUpdate(BaseModel):
    ...

class SubmissionView(Submission):
    user_id: int
    problem_id: int

    judger_id: Optional[int]

    evaluation_begin: Optional[datetime]
    evaluation_end: Optional[datetime]

    passed: Optional[int]
    failed: Optional[int]

    failed_wrong: Optional[int]
    failed_time: Optional[int]
    failed_space: Optional[int]
    failed_syntax: Optional[int]
    failed_other: Optional[int]

    weighted_sum: Optional[int]

    class Config:
        orm_mode = True