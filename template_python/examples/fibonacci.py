#!/usr/bin/env python3
"""Fibonacci numbers"""


def user_input() -> str:
    """Accept user input for Fibonacci function
    ---
    - Accept an integer from user input.
    - Throw exception if user inputs non-integer.
    """
    try:
        n = input("Please enter a number: ")
        return (
            f"Fibonacci number {n} is: {f(int(n))}. The full list is:\n{f_list(int(n))}"
        )
    except Exception as e:
        raise e


def f(n: int) -> int:
    """Return the nth Fibonacci number."""
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def f_list(n: int) -> list[int]:
    """Return a list of the first n Fibonacci numbers."""
    out = []
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        out.append(a)
    return out


if __name__ == "__main__":
    print(user_input())
