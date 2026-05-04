# keep calculated scores between 0 and 100
def clamp(value: int) -> int:
    return max(0, min(100, value))

# measure review activity: merged changes improve the score while abandoned changes reduce it
def activity_score(merged_90d: int, abandoned_90d: int) -> int:
    score = 30
    score += min(merged_90d * 3, 60)
    score -= min(abandoned_90d * 2, 25)
    return clamp(score)

# measures project participation using unique contributor count
def contribution_score(contributors: int) -> int:
    return clamp(20 + contributors * 8)

# measures review health: high merge ratio improves it while large / old backlogs reduce the score
def review_health_score(open_changes: int, average_age_days: float, merge_ratio: float) -> int:
    score = 100
    score -= min(open_changes // 2, 35)
    score -= min(int(average_age_days), 35)
    score += int(merge_ratio * 20)
    return clamp(score)

# combines three score areas into one weighted overall score
def overall_score(activity: int, contribution: int, review_health: int) -> int:
    return clamp(round(activity * 0.30 + contribution * 0.20 + review_health * 0.50))

# convert numerical health score into readable health label
def health_label(score: int) -> str:
    if score >= 80:
        return "Healthy"
    if score >= 60:
        return "Monitor"
    return "At Risk"