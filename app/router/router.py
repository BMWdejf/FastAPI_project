from fastapi import APIRouter, HTTPException
from sqlalchemy.future import engine
from sqlmodel import Session

from app.db.base import db
from app.models.person import Person, Sex
from app.repository.person import PersonRepo
from app.models.person_create import PersonCreate


router = APIRouter()

@router.on_event("startup")
async def startup():
    db.init()
    db.create_all()

@router.get("/person")
async def get_person():
    return db.get_session().query(PersonRepo.model).all()

@router.post("/create_person")
async def create_person_endpoint():
    pass

@router.on_event("shutdown")
async def shutdown():
    db.close()




