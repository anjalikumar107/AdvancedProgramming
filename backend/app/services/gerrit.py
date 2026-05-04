import json, httpx
from datetime import datetime, timezone, timedelta
from urllib.parse import quote_plus
from app.config import BASE_URL, REQUEST_TIMEOUT
from app.exceptions import ExternalApiError

# remove Gerrit's security prefix before JSON before parsing
def strip_gerrit_prefix(text: str) -> str:
    if text.startswith(")]}'"):
        return text.split("\n", 1)[1]
    return text

# query Gerrit's changes endpoint and return parsed change records
async def query_changes(query: str, limit: int = 100) -> list[dict]:
    encoded_query = quote_plus(query)
    url = f"{BASE_URL}/changes/?q={encoded_query}&n={limit}"
    try:
        async with httpx.AsyncClient(timeout=REQUEST_TIMEOUT) as client:
            response = await client.get(url)
    except httpx.TimeoutException as exc:
        raise ExternalApiError("Request timed out") from exc
    except httpx.HTTPError as exc:
        raise ExternalApiError("Request failed") from exc

    if response.status_code >= 400:
        raise ExternalApiError(f"Returned status {response.status_code}")
    try:
        return json.loads(strip_gerrit_prefix(response.text))
    except json.JSONDecodeError as exc:
        raise ExternalApiError("Returned invalid JSON") from exc

# return all open changes for the given Gerrit project
async def get_open_changes(project: str) -> list[dict]:
    return await query_changes(f"project:{project} status:open")

# return changes merged in the last 90 days for the given project
async def get_merged_changes(project: str) -> list[dict]:
    since = (datetime.now(timezone.utc) - timedelta(days=90)).date().isoformat()
    return await query_changes(f"project:{project} status:merged after:{since}")

# return changes abandoned in the last 90 days for the given project
async def get_abandoned_changes(project: str) -> list[dict]:
    since = (datetime.now(timezone.utc) - timedelta(days=90)).date().isoformat()
    return await query_changes(f"project:{project} status:abandoned after:{since}")