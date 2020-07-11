#!/usr/bin/env python3
"""Fibonacci numbers"""


def user_input():
    """Accept user input for Fibonacci function
    ---
    - Accept an integer from user input.
    - Throw exception if user inputs non-integer.
    """
    try:
        n = input("Please enter a number: ")
        print(f"Fibonacci number {n} is: {f(int(n))}")
        print(f"The full list is:\n{f_list(int(n))}")
    except Exception as e:
        print(f"An exception occurred:\n{e}\nPlease enter a number.")


def f(n):
    """Return the nth Fibonacci number."""
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def f_list(n):
    """Return a list of the first n Fibonacci numbers."""
    out = []
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        out.append(a)
    return out


if __name__ == "__main__":
    user_input()
