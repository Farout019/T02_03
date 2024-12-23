from sqlalchemy.orm import Session
from app.models.user import User
from app.repositories.user_repository import get_user_by_id, create_user


def fetch_user(db: Session, user_id: int):
    return get_user_by_id(db, user_id)


def add_user(db: Session, name: str, email: str, password: str):
    new_user = User(name=name, email=email, password=password)
    return create_user(db, new_user)
