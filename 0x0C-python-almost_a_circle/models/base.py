#!/usr/bin/python3
"""Defines a base model class."""
import json
import csv
import turtle


class Base:
    """Base model.

    This Represents the "base" for all other classes in project 0x0C*.

    Private Class Attributes:
        __nb_object (int): Number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base.

        Args:
            id (int): The identity of the new Base.
        """
        self.id = id if id is not None else type(self).__nb_objects + 1
        type(self).__nb_objects += 1

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON serialization of a list of dicts.

        Args:
            list_dictionaries (list): A list of dictionaries.
        """
        return json.dumps(list_dictionaries or [])

    @classmethod
    def save_to_file(cls, lst_objs):
        """Write the JSON serialization of a list of objects to a file.

        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".json"
        lst_dicts = [o.to_dictionary() for o in lst_objs] if lst_objs else []
        with open(filename, "w") as jsonfile:
            jsonfile.write(Base.to_json_string(lst_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return the deserialization of a JSON string.

        Args:
            json_string (str): A JSON str representation of a list of dicts.
        Returns:
            If json_string is None or empty - an empty list.
            Otherwise - the Python list represented by json_string.
        """
        return json.loads(json_string or "[]")

    @classmethod
    def create(cls, **dictionary):
        """Return a class instantiated from a dictionary of attributes.

        Args:
            **dictionary (dict): Key/value pairs of attributes to initialize.
        """
        if dictionary:
            new = cls(1, 1) if cls.__name__ == "Rectangle" else cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """Return a list of classes instantiated from a file of JSON strings.

        Reads from `<cls.__name__>.json`.

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = f"{cls.__name__}.json"
        try:
            with open(filename, "r") as jsonfile:
                lst_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in lst_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, lst_objs):
        """Write the CSV serialization of a list of objects to a file.

        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".csv"
        fieldnames = (
            ["id", "width", "height", "x", "y"] if cls.__name__ == "Rectangle"
            else ["id", "size", "x", "y"]
        )
        lst_dicts = ([obj.to_dictionary()
                     for obj in lst_objs] if lst_objs else [])
        with open(filename, "w", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            for obj_dict in lst_dicts:
                writer.writerow(obj_dict)

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a CSV file.

        Reads from `<cls.__name__>.csv`.

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = f"{cls.__name__}.csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                fieldnames = (
                    ["id", "width", "height", "x", "y"]
                    if cls.__name__ == "Rectangle"
                    else ["id", "size", "x", "y"]
                )
                lst_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                lst_dicts = ([dict([k, int(v)]
                             for k, v in d.items()) for d in lst_dicts])
                return [cls.create(**d) for d in lst_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module.

        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        def draw_object(obj, color):
            turt.color(color)
            turt.showturtle()
            turt.up()
            turt.goto(obj.x, obj.y)
            turt.down()
            for _ in range(2):
                turt.forward(obj.width)
                turt.left(90)
                turt.forward(obj.height)
                turt.left(90)
            turt.hideturtle()

        for rect in list_rectangles:
            draw_object(rect, "#ffffff")

        for sq in list_squares:
            draw_object(sq, "#b5e3d8")

        turtle.exitonclick()
