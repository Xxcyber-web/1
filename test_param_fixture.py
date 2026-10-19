import pytest


@pytest.fixture(params=[10, 20, 30])
def number(request):
    return request.param


def test_number_is_positive(number):
    assert number > 0