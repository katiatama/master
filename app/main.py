from fastapi import FastAPI
from app.api.health import router as health_router

app = FastAPI(title="DevOps FastAPI App")


@app.get("/")
def read_root():
    return {"message": "Hello World"}


app.include_router(health_router)
