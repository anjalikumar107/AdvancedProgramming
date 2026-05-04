import pytest
from pydantic import ValidationError
from app.models.models import ProjInput

def test_valid_project_name():
    # create model with a valid gerrit project path
    model = ProjInput(project="platform/build")
    # check the value is accepted and stored correctly
    assert model.project == "platform/build"

def test_invalid_project_name():
    # expect ValidationError to be raised by Pydantic validator
    with pytest.raises(ValidationError):
        ProjInput(project="invalid project name")
        