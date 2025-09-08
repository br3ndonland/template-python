import pytest

from template_python.examples import palindrome


@pytest.mark.parametrize(
    ("input_string", "is_a_palindrome"),
    (("racecar", True), ("A man, A Plan, A Canal, Panama", True), ("Foo bar", False)),
)
def test_palindrome(input_string: str, is_a_palindrome: bool) -> None:
    if is_a_palindrome:
        expected_result = f"The input {input_string} is a palindrome."
    else:
        expected_result = f"The input {input_string} is not a palindrome."
    result = palindrome.process_user_input(input_string)
    assert result == expected_result


def test_palindrome_incorrect_input_type() -> None:
    with pytest.raises(AttributeError):
        _ = palindrome.process_user_input([])  # pyright: ignore[reportArgumentType]
