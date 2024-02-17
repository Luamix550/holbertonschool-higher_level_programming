#!/usr/bin/python3
"""
This module contains a class Square that defines a square.
"""


class Square:
    """
    This class defines a square with a private instance attribute size.
    """

    def __init__(self, size=0):
        """
        Initializes a square with a given size.

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Computes the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
