#!/usr/bin/python3
"""Square module."""


class Square:
    """Defines a square with size and position attributes."""

    def __init__(self, size=0, position=(0, 0)):
        """Constructor.
        Args:
            size: Length of side of the square (default is 0).
            position: Tuple of 2 positive integers representing the position
                      (default is (0, 0)).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter method to retrieve the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method to set the size."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Getter method to retrieve the position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter method to set the position."""
        if not isinstance(value, tuple) or len(value) != 2 \
                or not all(isinstance(i, int) for i in value) \
                or any(i < 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Calculate the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the character #."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
