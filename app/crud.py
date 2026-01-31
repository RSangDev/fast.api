from sqlalchemy.orm import Session
from app import models, schemas

from app.models import User
from app.schemas import UserCreate, UserUpdate


def create_user(db: Session, user: UserCreate):
    db_user = User(
        name=user.name,
        email=user.email
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_users(db: Session):
    return db.query(User).all()


def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def update_user(db: Session, user_id: int, user: UserUpdate):
    db_user = get_user_by_id(db, user_id)

    if not db_user:
        return None

    if user.name is not None:
        db_user.name = user.name
    if user.email is not None:
        db_user.email = user.email

    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, user_id: int):
    db_user = get_user_by_id(db, user_id)

    if not db_user:
        return None

    db.delete(db_user)
    db.commit()
    return db_user
