import pytest
from ..main.app import longest_unique_substring

def test_empty_string():
    assert longest_unique_substring("") == 0


def test_single_character():
    assert longest_unique_substring("A") == 1


def test_no_repetition():
    assert longest_unique_substring("ABCDE") == 5


def test_with_repetition():
    assert longest_unique_substring("ABCABCFKAB") == 5


def test_all_same_character():
    assert longest_unique_substring("AAAAAA") == 1


def test_mixed_case():
    assert longest_unique_substring("AaAaAa") == 2


def test_numbers_and_symbols():
    assert longest_unique_substring("123@123@") == 4


def test_long_string():
    assert longest_unique_substring("abcabcbb") == 3

@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("ABCABCFKAB", 5)
    ]
)
def test_parametrized(input_str, expected):
    assert longest_unique_substring(input_str) == expected