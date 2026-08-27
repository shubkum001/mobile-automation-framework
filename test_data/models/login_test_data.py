from dataclasses import dataclass


@dataclass(frozen=True)
class LoginTestData:
    test_case: str
    username: str
    password: str
    expected_result: str