from fastapi import FastAPI

app = FastAPI(title="Gerrit Project Health Dashboard")


@app.get("/api/health")
async def health():
    return {"status": "ok"}