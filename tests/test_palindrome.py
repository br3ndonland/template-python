from examples import palindrome


def test_palindrome_01():
    assert palindrome.palindrome("racecar") is True


def test_palindrome_02():
    assert palindrome.palindrome("A man, A Plan, A Canal, Panama") is True


def test_palindrome_03():
    assert palindrome.palindrome("Foo bar") is False


def test_palindrome_04():
    assert palindrome.palindrome([]) is False
