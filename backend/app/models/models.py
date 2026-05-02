import re
from pydantic import BaseModel, Field, field_validator

PATTERN = re.compile(r"^[A-Za-z0-9_.\-/]+$")

class ProjInput(BaseModel):
    project: str = Field(..., examples=[
        "platform/build",
        "platform/system/core",
        "platform/frameworks/base",
        ])
    @field_validator("project")
    @classmethod
    def validate_project(cls, value: str) -> str:
        # reject invalid project names before making Gerrit API requests
        if not PATTERN.match(value):
            raise ValueError("Enter a valid Gerrit project path")
        return value

class ProjSummary(BaseModel):
    team: str
    project: str
    url: str
    open_changes: int
    merged_changes_30d: int
    abandoned_changes_30d: int
    active_contributors: int
    average_open_change_age_days: float
    merge_ratio: float
    abandonment_ratio: float
    activity_score: int
    contribution_score: int
    review_health_score: int
    overall_health_score: int
    health_label: str