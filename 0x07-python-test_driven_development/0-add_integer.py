#!/usr/bin/python3
"""Defines an add_integer function."""


def add_integer(a, b=98):
    """Add two integers.

    Args:
        a (int): The first integer.
        b (int): The second integer (default is 98).

    Returns:
        int: The sum of a and b.

    Raises:
        TypeError: If a or b is not an integer.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
