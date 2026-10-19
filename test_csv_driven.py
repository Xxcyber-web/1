import csv
from pathlib import Path

import pytest
from validate import validate_login


with open(
    Path(__file__).with_name("logins.csv"),
    newline="",
    encoding="utf-8",
) as file:
    test_cases = list(csv.DictReader(file))


@pytest.mark.parametrize("case", test_cases)
def test_login_from_csv(case):
    username = case["username"]
    password = case["password"]
    expected = case["expected"].lower() == "true"

    assert validate_login(username, password) == expected