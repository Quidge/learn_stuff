import pytest

from base import rating

_voyage = {"zone": "china", "length": 10}
_history = [
    {
        "zone": "east-indies",
        "profit": 5
    },
    {
        "zone": "west-indies",
        "profit": 15
    },
    {
        "zone": "china",
        "profit": -2
    },
    {
        "zone": "west-africa",
        "profit": 7
    },
]


@pytest.fixture
def voyage():
    return _voyage


@pytest.fixture
def history():
    return _history


def test_rating(voyage, history):
    assert rating(voyage, history) == "A"
