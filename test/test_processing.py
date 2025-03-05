import pytest
from src.processing import filter_by_state, sort_by_date

@pytest.fixture
def sample_data():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14"},
    ]

def test_filter_by_state_executed(sample_data):
    expected = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30"},
    ]
    assert filter_by_state(sample_data, "EXECUTED") == expected

def test_filter_by_state_canceled(sample_data):
    expected = [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14"},
    ]
    assert filter_by_state(sample_data, "CANCELED") == expected

@pytest.mark.parametrize(
    "state, expected_count",
    [
        ("EXECUTED", 2),
        ("CANCELED", 2),
        ("PENDING", 0),
        ("", 0),
    ]
)
def test_filter_by_state_parametrized(sample_data, state, expected_count):
    result = filter_by_state(sample_data, state)
    assert len(result) == expected_count

def test_sort_by_date_same_dates():
    data = [
        {"id": 1, "date": "2023-01-01"},
        {"id": 2, "date": "2023-01-01"},
        {"id": 3, "date": "2023-01-01"},
    ]
    expected = [
        {"id": 1, "date": "2023-01-01"},
        {"id": 2, "date": "2023-01-01"},
        {"id": 3, "date": "2023-01-01"},
    ]
    assert sort_by_date(data) == expected

def test_sort_by_date_invalid_format():
    data = [
        {"id": 1, "date": "2023-01-01"},
        {"id": 2, "date": "invalid-date"},
        {"id": 3, "date": "2023-01-02"},
    ]
    with pytest.raises(ValueError):
        sort_by_date(data)
