import json
from pathlib import Path

from test_data.models.login_test_data import LoginTestData


def load_login_test_data(platform: str) -> list[LoginTestData]:

    file_path = (
        Path(__file__).resolve().parent.parent
        / "test_data"
        / platform
        / "login_data.json"
    )

    with open(file_path, "r", encoding="utf-8") as file:
        raw_data = json.load(file)

    return [
        LoginTestData(**item)
        for item in raw_data
    ]                                                               # this is List comphrehension


