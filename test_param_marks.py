import pytest


@pytest.mark.parametrize(
    "number, expected",
    [
        (2, 4),
        (3, 9),
        (4, 16),
        pytest.param(
            5,
            20,
            marks=pytest.mark.xfail,
            id="expected-failure",
        ),
    ],
)
def test_square(number, expected):
    assert number * number == expected