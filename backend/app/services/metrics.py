from datetime import datetime, timezone

# convert gerrit timestamp into a python datetime
def parse_gerrit_date(value: str) -> datetime:
    clean = value.split(".")[0]
    return datetime.strptime(clean, "%Y-%m-%d %H:%M:%S").replace(tzinfo=timezone.utc)

# return a contributor identifier from a Gerrit change
def owner_id(change: dict) -> str:
    owner = change.get("owner", {})
    return str(
        owner.get("_account_id")
        or owner.get("email")
        or owner.get("name")
        or "unknown"
    )

# get a contributer identifier from a gerrit change
def active_contributors(changes: list[dict]) -> int:
    """Count unique contributors across a list of Gerrit changes."""
    return len({owner_id(change) for change in changes})

# calculate the average age of open changes in days. the actual backlog age is measured so created date is used first
def average_open_change_age(open_changes: list[dict]) -> float:
    if not open_changes:
        return 0.0

    now = datetime.now(timezone.utc)
    ages = []

    for change in open_changes:
        date_value = change.get("created") or change.get("updated")
        if not date_value:
            continue
        try:
            ages.append((now - parse_gerrit_date(date_value)).days)
        except ValueError:
            continue
    if not ages:
        return 0.0

    return round(sum(ages) / len(ages), 1)