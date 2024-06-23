from datetime import date
from typing import Optional
from enum import Enum
from sqlalchemy import Enum as SQLAlchemyEnum
from sqlmodel import SQLModel, Field
from app.models.mixins import TimeMixin

class Sex(str, Enum):
    MALE = "male"
    FEMALE = "female"

class Person(SQLModel, TimeMixin, table=True):
    __tablename__ = "person"

    id: Optional[int] = Field(default=None, primary_key=True, nullable=False)
    name: Optional[str]
    birth: date
    sex: Sex = Field(sa_column=SQLAlchemyEnum(Sex))
    profile: str
    phone_number: int

    class Config:
        arbitrary_types_allowed = True