from datetime import datetime, timezone
from app.models.models import ProjSummary
from app.services.scoring import overall_score, health_label

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

# convert gerrit data into project summary
def summary(project_config, open_changes, merged_changes, abandoned_changes):
    total_closed = max(len(merged_changes) + len(abandoned_changes), 1)
    # calculate merge ratio
    merge_ratio = len(merged_changes) / total_closed
    # scoring using merge ratio
    overall = overall_score(50, 50, int(merge_ratio * 100))
    return ProjSummary(
        team=project_config["team"],
        project=project_config["project"],
        url=project_config["url"],
        open_changes=len(open_changes),
        merged_changes_90d=len(merged_changes),
        abandoned_changes_90d=len(abandoned_changes),
        active_contributors=0,
        average_open_change_age_days=0,
        merge_ratio=merge_ratio,
        abandonment_ratio=1 - merge_ratio,
        activity_score=50,
        contribution_score=50,
        review_health_score=int(merge_ratio * 100),
        overall_health_score=overall,
        health_label=health_label(overall),
    )