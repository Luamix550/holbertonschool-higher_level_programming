#!/usr/bin/python3
"""
This module contains a class Square that defines a square.
"""


class Square:
    """
    This class defines a square with a private instance attribute size.
    """

    def __init__(self, size):
        """
        Initializes a square with a given size.

        Args:
            size (int): The size of the square.

        Attributes:
            __size (int): The size of the square.
        """
        self.__size = size
