import pytest
from utils.radix import radix_sort_phone_numbers


@pytest.fixture
def sample_data():
    return [
        ("+123-456-1234567", "John"),
        ("+456-789-2345678", "Alice"),
        ("+789-123-3456789", "Bob"),
        (
            "+7-495-1123212",
            "n399tann9nnt3ttnaaan9nann93na9t3a3t9999na3aan9antt3tn93aat3naatt"
        ),
        ("+123-789-4567890", "Eve"),
        ("+456-123-5678901", "Charlie")
    ]


def test_radix_sort_phone_numbers(sample_data):
    sorted_data = radix_sort_phone_numbers(sample_data)
    assert sorted_data == [
        (
            "+7-495-1123212",
            "n399tann9nnt3ttnaaan9nann93na9t3a3t9999na3aan9antt3tn93aat3naatt"
        ),
        ("+123-456-1234567", "John"),
        ("+123-789-4567890", "Eve"),
        ("+456-123-5678901", "Charlie"),
        ("+456-789-2345678", "Alice"),
        ("+789-123-3456789", "Bob")
    ]


def test_radix_sort_phone_numbers_empty():
    empty_data = []
    sorted_data = radix_sort_phone_numbers(empty_data)
    assert sorted_data == []


def test_radix_sort_phone_numbers_single_element():
    single_data = [("+123-456-7890", "John")]
    sorted_data = radix_sort_phone_numbers(single_data)
    assert sorted_data == [("+123-456-7890", "John")]


def test_radix_sort_phone_numbers_already_sorted(sample_data):
    sorted_data = radix_sort_phone_numbers(sample_data)
    re_sorted_data = radix_sort_phone_numbers(sorted_data)
    assert sorted_data == re_sorted_data
