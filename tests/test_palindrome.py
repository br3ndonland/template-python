import pytest

from examples import palindrome


def test_palindrome_01() -> bool:
    test = palindrome.prep_input("racecar")
    assert test is True
    return test


def test_palindrome_02() -> bool:
    test = palindrome.prep_input("A man, A Plan, A Canal, Panama")
    assert test is True
    return test


def test_palindrome_03() -> bool:
    test = palindrome.prep_input("Foo bar")
    assert test is False
    return test


def test_palindrome_04() -> bool:
    test = palindrome.prep_input("[]")
    assert test is False
    return test


def test_palindrome_05() -> bool:
    with pytest.raises(AttributeError):
        assert palindrome.prep_input([]) is False  # type: ignore
        raise
