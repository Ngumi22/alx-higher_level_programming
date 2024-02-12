#!/usr/bin/python3
"""Defines a base model class."""

class Base:
    """private class attribute"""

    __nb_objects = 0
    
    """class constructor"""

    def __init__(self, id=None):
        """
        If id is not provided, increment __nb_objects and assign to id

        Args:
            id (int): The identity of the new Base.
        """

        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            """assign provided id to the public instance attribute id"""

            self.id = id
