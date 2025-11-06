import pytest
from consecutive_numbers.main.app import has_n_consecutive_ones_circular

@pytest.mark.parametrize(
    "s,n,expected",
    [
        ("1111000", 4, True),
        ("1010111", 4, True),
        ("1101101", 4, False),
        ("0000000", 1, False),
        ("1", 1, True),
        ("111", 3, True),
        ("111", 4, False),  # n > len -> False
        ("1010101", 2, True), # "11" in circular
        ("0111010", 3, True),  # has "111" in middle
    ]
)
def test_various_cases(s, n, expected):
    assert has_n_consecutive_ones_circular(s, n) == expected

def test_invalid_n():
    with pytest.raises(ValueError):
        has_n_consecutive_ones_circular("1010", 0)

def test_invalid_string():
    with pytest.raises(ValueError):
        has_n_consecutive_ones_circular("10a01", 2)
