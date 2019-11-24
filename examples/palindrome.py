#!/usr/bin/env python3
"""Palindromes"""
import re


def user_input():
    """Clean and validate user input for palindrome function
    ---
    - Convert user input string to lowercase.
    - Remove any characters other than word and digit.
    - Verify that length is at least 3 characters.
    """
    try:
        user = input("Please provide an input to test: ").lower()
        string = re.sub(r"[^\w\d]", "", user)
        if len(string) > 2:
            palindrome(string)
    except Exception as e:
        print(f"An exception occurred:\n{e}\nPlease try again.")


def palindrome(string):
    """Identify palindromes
    ---
    - Accept a string from user input, after validation.
    - Create a new object with the reversed string.
    - Compare forward and reversed strings.
    """
    backwards = string[::-1]
    if string == backwards:
        print(f"Success! The input {string} is a palindrome.")
    else:
        print(f"The input {string} is not a palindrome.")


if __name__ == "__main__":
    user_input()
