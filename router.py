# from config import loop, KAFKA_BOOTSTRAP_SERVERS, KAFKA_CONSUMER_GROUP, KAFKA_TOPIC
import json
from sqlalchemy.orm import Session
from fastapi import Depends, APIRouter
from core.db import get_db
from crud.data_crud import UserDataCRUD
from schema import PersonDataSchema, PersonDataDataSchema


router = APIRouter(
    prefix="/person",
    responses={404: {"description": "Sorry Not found"}},
)


@router.get("/{data_id}", response_model=PersonDataDataSchema)
def data(data_id: int, db: Session = Depends(get_db)) -> PersonDataDataSchema:
    data_crud = UserDataCRUD()
    # Для синхронного запуска
    data_i = data_crud.get(db, data_id)
    return data_i


@router.post("/", response_model=PersonDataDataSchema)
def create(data: PersonDataSchema, db: Session = Depends(get_db)):
    data_crud = UserDataCRUD()
    # Для синхронного запуска
    data_i = data_crud.create(db, **data.dict(exclude_unset=True))
    return data_i
