#!/usr/bin/env python3
"""Palindromes"""

import re


def user_input() -> str:
    """Accept a string from user input."""
    try:
        user_input_string = input("Please provide an input to test: ")
        return process_user_input(user_input_string)
    except Exception:
        raise


def process_user_input(string: str) -> str:
    """Clean and validate user input for palindrome function
    ---
    - Convert user input string to lowercase.
    - Remove any characters other than word and digit.
    - Verify that length is at least 3 characters.
    """
    processed_string = re.sub(r"[^\w\d]", "", string.lower())
    if len(processed_string) > 2 and palindrome(processed_string):
        message = f"The input {string} is a palindrome."
    else:
        message = f"The input {string} is not a palindrome."
    print(message)
    return message


def palindrome(s: str) -> bool:
    """Identify palindromes
    ---
    - Accept a string from user input, after validation.
    - Create a new object with the reversed string.
    - Compare forward and reversed strings.
    """
    backwards = s[::-1]
    return s == backwards


if __name__ == "__main__":
    print(user_input())
