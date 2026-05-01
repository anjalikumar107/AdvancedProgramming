from fastapi import FastAPI

app = FastAPI(title="Android Gerrit Team Health Dashboard")


@app.get("/api/health")
async def health():
    return {"status": "ok"}