from fastapi import FastAPI
from app.routers import user, product
from app.db import engine, Base

# Create tables on startup (if they don't exist)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="My Store API")

# Include routers with proper prefixes
app.include_router(user.router, prefix="/users", tags=["Users"])
app.include_router(product.router, prefix="/products", tags=["Products"])

# Optional root endpoint
@app.get("/")
def root():
    return {"message": "Welcome to My Store API"}

