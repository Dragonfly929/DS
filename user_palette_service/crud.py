from sqlalchemy.orm import Session
from .models import User, Palette

def create_user(db: Session, username: str, password_hash: str):
    user = User(username=username, password_hash=password_hash)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def create_palette(db: Session, user_id: int, color_codes: list, category: str):
    palette = Palette(user_id=user_id, color_codes=color_codes, category=category)
    db.add(palette)
    db.commit()
    db.refresh(palette)
    return palette
