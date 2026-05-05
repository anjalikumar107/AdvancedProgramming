from fastapi import APIRouter
from app.config import PROJECTS
from app.services.gerrit import get_abandoned_changes, get_merged_changes, get_open_changes
from app.services.metrics import summary

router = APIRouter(prefix="/api")

# return health summaries for all configured projects
@router.get("/projects")
async def projects():
    results = []
    for project in PROJECTS:
        open_changes = await get_open_changes(project["project"])
        merged = await get_merged_changes(project["project"])
        abandoned = await get_abandoned_changes(project["project"])
        results.append(summary(project, open_changes, merged, abandoned))
    return results
