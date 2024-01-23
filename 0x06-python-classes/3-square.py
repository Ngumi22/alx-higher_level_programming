#!/usr/bin/python3
"""Square module."""


class Square:
    """Defines a square with optional size attribute."""

    def __init__(self, size=0):
        """Constructor.
        Args:
            size: Length of side of the square (default is 0).
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Calculate the area of the square."""
        return self.__size ** 2
