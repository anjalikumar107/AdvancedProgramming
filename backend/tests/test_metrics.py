from app.services.metrics import active_contributors, average_open_change_age

# two different contributors (contributor 1 and contributor 2)
def test_active_contributors():
    changes = [
        {"owner": {"_account_id": 1}},
        {"owner": {"_account_id": 2}},
    ]
    assert active_contributors(changes) == 2

# no changes should return zero
def test_average_open_change_age_empty():
    assert average_open_change_age([]) == 0.0