from fastapi import FastAPI
from app.projects import router

app = FastAPI(title="Android Gerrit Team Health Dashboard")

@app.get("/api/health")
async def health():
    return {"status": "ok"}

app.include_router(router)