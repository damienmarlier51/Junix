import json
from pathlib import Path

import pytest

TEST_DIR = Path(__file__).resolve().parents[0]


@pytest.fixture
def notebook_as_json():

    with open(f"{TEST_DIR}/test.json", "r") as f:
        return json.load(f)
