# ~/My_store/apps/backend/app/main.py
from fastapi import FastAPI
from app.database import engine, Base
from app.routers import user  # new user router
# from app.api import auth, products  # uncomment when ready

# Create DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="My Store API")

# Include routers
app.include_router(user.router, prefix="/users", tags=["users"])
# app.include_router(auth.router, prefix="/auth", tags=["auth"])
# app.include_router(products.router, prefix="/products", tags=["products"])

@app.get("/")
def read_root():
    return {"message": "Welcome to My_store Backend API"}

