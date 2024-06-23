# app/models/person_create.py
from datetime import date
from pydantic import BaseModel, validator
from app.models.person import Sex

class PersonCreate(BaseModel):
    name: str
    birth: date
    sex: str
    profile: str
    phone_number: int

    @validator('sex')
    def validate_sex(cls, v):
        if v not in Sex.__members__.values():
            raise ValueError('Invalid sex value')
        return v
