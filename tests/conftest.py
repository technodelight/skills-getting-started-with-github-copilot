from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src.app import app, activities as activities_db

INITIAL_ACTIVITIES = deepcopy(activities_db)

@pytest.fixture(autouse=True)
def reset_activities():
    activities_db.clear()
    activities_db.update(deepcopy(INITIAL_ACTIVITIES))
    yield

@pytest.fixture
def client():
    return TestClient(app)
