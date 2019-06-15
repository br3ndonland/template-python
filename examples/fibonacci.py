#!/usr/bin/env python3
"""Fibonacci numbers"""


def user_input():
    """Accept an integer from user input.
    Throw exception if user inputs non-integer.
    """
    try:
        n = input("Please enter a number: ")
        print(f"Fibonacci number {n} is: {f(int(n))}")
    except Exception as e:
        print(f"An exception occurred:\n{e}\nPlease enter a number.")


def f(n):
    """Return the nth Fibonacci number."""
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    return a


if __name__ == "__main__":
    user_input()
