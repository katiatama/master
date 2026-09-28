from fastapi import FastAPI
<<<<<<< HEAD

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/health")
def health():
    return {"status": "ok"}
=======
from app.api.health import router as health_router

app = FastAPI(title="DevOps FastAPI App")

app.include_router(health_router)
>>>>>>> ef687b8 (feat: create FastAPI application with tests)
