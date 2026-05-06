from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.projects import router

app = FastAPI(title="Android Gerrit Team Health Dashboard")

# allow the  frontend to call the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

@app.get("/api/health")
async def health():
    return {"status": "ok"}