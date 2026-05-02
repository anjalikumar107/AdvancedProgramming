import pytest
from pydantic import ValidationError
from app.models.models import ProjInput

def test_valid_project_name():
    model = ProjInput(project="platform/build")
    assert model.project == "platform/build"

def test_invalid_project_name():
    with pytest.raises(ValidationError):
        ProjInput(project="invalid project name")