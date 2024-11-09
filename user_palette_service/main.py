from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from werkzeug.security import generate_password_hash, check_password_hash  # Import from Werkzeug
from .database import SessionLocal, engine
from . import models, crud
from .grpc_client import get_popular_palettes

app = FastAPI()

# Dependency to get the DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Route to register a user with hashed password
@app.post("/users/register")
async def register_user(username: str, password: str, db: Session = Depends(get_db)):
    # Use Werkzeug to hash the password securely
    password_hash = generate_password_hash(password)
    user = crud.create_user(db, username=username, password_hash=password_hash)
    return {"user_id": user.user_id, "username": user.username}

@app.post("/palettes")
async def create_palette(user_id: int, color_codes: list, category: str, db: Session = Depends(get_db)):
    palette = crud.create_palette(db, user_id=user_id, color_codes=color_codes, category=category)
    return {"palette_id": palette.palette_id, "user_id": palette.user_id, "category": palette.category}
