import pytest

from examples import palindrome


def test_palindrome_01() -> None:
    assert palindrome.prep_input("racecar") is True


def test_palindrome_02() -> None:
    assert palindrome.prep_input("A man, A Plan, A Canal, Panama") is True


def test_palindrome_03() -> None:
    assert palindrome.prep_input("Foo bar") is False


def test_palindrome_04() -> None:
    assert palindrome.prep_input("[]") is False


def test_palindrome_05() -> None:
    with pytest.raises(AttributeError):
        assert palindrome.prep_input([]) is False  # type: ignore
        raise
