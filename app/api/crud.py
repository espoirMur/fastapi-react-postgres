from sqlalchemy.orm import Session
from api.models import User
from api.schemas import User as UserSchema
from typing import List 


class UserManager:

    def __init__(self, session: Session) -> None:
        self.database_session = session

    def get_users(self) -> List[User]:
        return self.database_session.query(User).all()
