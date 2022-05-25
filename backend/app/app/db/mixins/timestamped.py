from sqlalchemy import Column, DateTime
from sqlalchemy.sql.functions import now

class TimestampedMixin(object):
    created_at = Column(DateTime, default=now())
    updated_at = Column(DateTime, default=now(), onupdate=now())