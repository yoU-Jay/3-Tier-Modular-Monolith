# services/user_service.py
from backend.models.user import User, UserCreate
from typing import List

# Temporary in-memory "database"
fake_user_db: List[User] = []

class UserService:
    def __init__(self):
        self.db = fake_user_db

    def create_user(self, user: User) -> User:
        self.db.append(user)
        return user

    def list_users(self) -> List[User]:
        return self.db
