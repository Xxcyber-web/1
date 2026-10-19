import pytest
from mathutils import factorial


@pytest.mark.parametrize(
    "n, expected",
    [
        pytest.param(0, 1, id="zero"),
        pytest.param(1, 1, id="one"),
        pytest.param(3, 6, id="three"),
        pytest.param(5, 120, id="five"),
    ],
)
def test_factorial_with_ids(n, expected):
    assert factorial(n) == expected