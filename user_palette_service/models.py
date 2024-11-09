from sqlalchemy import Column, Integer, String, TIMESTAMP, JSON, ForeignKey
from .database import Base

class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password_hash = Column(String)
    created_at = Column(TIMESTAMP)

class Palette(Base):
    __tablename__ = "palettes"
    palette_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    color_codes = Column(JSON)
    category = Column(String)
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)
