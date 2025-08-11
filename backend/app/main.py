from fastapi import FastAPI

app = FastAPI(title="My Shop API")

@app.get("/")
async def read_root():
    return {"message": "Hello from My Shop API"}

