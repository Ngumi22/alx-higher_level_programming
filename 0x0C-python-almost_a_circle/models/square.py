#!/usr/bin/python3
"""Defines a square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get/set the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.validate_integer(value, "size")
        self.validate_positive(value, "size")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the Square."""
        if args:
            self.id = args[0] if args[0] is not None else self.id
            self.size = args[1] if len(args) > 1 else self.size
            self.x = args[2] if len(args) > 2 else self.x
            self.y = args[3] if len(args) > 3 else self.y

        elif kwargs:
            self.id = kwargs.get("id", self.id)
            self.size = kwargs.get("size", self.size)
            self.x = kwargs.get("x", self.x)
            self.y = kwargs.get("y", self.y)

    def to_dictionary(self):
        """Return the dictionary representation of the Square."""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return the print() and str() representation of a Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.size)

    def validate_integer(self, value, attribute):
        """Validate if a value is an integer."""
        if not isinstance(value, int):
            raise TypeError(f"{attribute} must be an integer")

    def validate_positive(self, value, attribute):
        """Validate if a value is positive."""
        if value <= 0:
            raise ValueError(f"{attribute} must be > 0")
