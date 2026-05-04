from app.services.scoring import overall_score, health_label

# ensure overall score calculation works as expected
def test_overall_score():
    assert overall_score(80, 70, 90) == 83

# test health label boundaries
def test_health_label():
    assert health_label(85) == "Healthy"
    assert health_label(65) == "Monitor"
    assert health_label(40) == "At Risk"