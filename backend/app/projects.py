from fastapi import APIRouter
from app.config import PROJECTS
from app.services.gerrit import get_abandoned_changes, get_merged_changes, get_open_changes
from app.services.metrics import summary
from app.config import PROJECTS, CACHE_SECONDS
from app.services.cache import get_cache, set_cache

router = APIRouter(prefix="/api")

# return health summaries for all configured projects and use cached health summaries when possible
@router.get("/projects")
async def projects():
    cached = get_cache("projects")
    if cached:
        return cached
    
    results = []
    for project in PROJECTS:
        open_changes = await get_open_changes(project["project"])
        merged = await get_merged_changes(project["project"])
        abandoned = await get_abandoned_changes(project["project"])
        results.append(summary(project, open_changes, merged, abandoned))
    
    set_cache("projects", results, CACHE_SECONDS)
    return results
