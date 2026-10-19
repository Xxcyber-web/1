import json
from pathlib import Path

import pytest
from mathutils import factorial

with open(
    Path(__file__).with_name("test_cases.json"),
    encoding="utf-8"
) as file:
    test_cases = json.load(file)


@pytest.mark.parametrize("case", test_cases)
def test_factorial_from_json(case):
    number = case["number"]
    expected = case["expected"]

    assert factorial(number) == expected