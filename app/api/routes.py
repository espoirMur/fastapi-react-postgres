from api.schemas import User
from fastapi import APIRouter
from typing import List
from api.database import SessionClass
from api.crud import UserManager

router = APIRouter()

@router.get("/users", response_model=List[User])
def read_user():
    with SessionClass() as database_session:
        user_manager = UserManager(database_session)
        return user_manager.get_users()
