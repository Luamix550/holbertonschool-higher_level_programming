#!/usr/bin/python3
"""
Defines the Base class with a private class
"""


class Base:
    """
    Represents a generic base class.

    Attributes:
        __nb_objects (int): Private class attribute
    Methods:
        __init__: Initializes an instance of Base.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes an instance of Base.

        Args:
            id (int, optional): ID for the instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
