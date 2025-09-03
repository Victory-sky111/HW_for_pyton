import pytest
from string_utils import StringUtils

string_utils = StringUtils()


@pytest.mark.parametrize("input_str, expected", [
    ("1010", "1010"),
    ("sky pro", "Sky pro"),
    ("s", "S"),
    ("", ""),
    (" ", " ")
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.parametrize("input_str,expected", [
    ("skypro", "skypro"),
    ("   skypro", "skypro"),
    ("skypro   ", "skypro   "),
    ("", ""),
    ("   ", "")
])
def test_trim(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.parametrize("string, symbol,expected,", [
    ("SkyPro", "S", True),
    ("SkyPro", "Sky", True),
    ("1010sky", "1", True),
    ("SkyPro", "A", False),
    ("", "S", False),
])
def test_contains(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected


@pytest.mark.parametrize("string,symbol,expected", [
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Pro", "Sky"),
    ("sss", "s", ""),
    ("SkyPro", "a", "SkyPro"),
    ("SkyPro", "", "SkyPro"),
    ("", "a", ""),
    ("102030", "1", "02030"),
])
def test_delete_symbol(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected
