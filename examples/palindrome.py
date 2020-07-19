#!/usr/bin/env python3
"""Palindromes"""
import re


def user_input() -> str:
    """Clean and validate user input for palindrome function
    ---
    - Convert user input string to lowercase.
    - Remove any characters other than word and digit.
    - Verify that length is at least 3 characters.
    """
    try:
        user = input("Please provide an input to test: ").lower()
        s = re.sub(r"[^\w\d]", "", user)
        if len(s) > 2 and palindrome(s):
            return f"Success! The input {s} is a palindrome."
        else:
            return f"The input {s} is not a palindrome."
    except Exception as e:
        return f"An exception occurred:\n{e}\nPlease try again."


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
