import pytest


@pytest.fixture(params=["Chrome", "Firefox", "Edge"])
def browser(request):
    return request.param


def test_browser_name(browser):
    assert browser in ["Chrome", "Firefox", "Edge"]