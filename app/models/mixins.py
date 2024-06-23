from datetime import datetime
from pydantic import BaseModel, Field
from sqlalchemy import Column, DateTime


class TimeMixin(BaseModel):

    created_at: datetime = Field(default_factory=datetime.now)
    modified_at: datetime = Field(
        sa_column = Column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
    )

    class Config:
        arbitrary_types_allowed = True