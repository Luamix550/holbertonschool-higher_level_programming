#!/usr/bin/python3
"""This is the Rectangle module.


"""
from models.base import Base


class Rectangle(Base):
    """This class inherits from Base and defines a Rectangle object.

    Attributes:
        __width (int): the width of the rectangle.
        __height (int): the height of the rectangle.
        __x (int): the horizontal (x) padding of the rectangle.
        __y (int): the vertical (y) padding of the rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the default attributes of the Base object.

        Args:
            width (int): the wanted width of the rectangle.
            height (int): the wanted height of the rectangle.
            x (int): the wanted horizontal (x) padding of the rectangle.
            y (int): the wanted vertical (y) padding of the rectangle.
            id (int): the wanted identifier of the Base object.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    # width attribute getter and setter.
    @property
    def width(self):
        """Get and Set the width attribute of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    # height attribute getter and setter.
    @property
    def height(self):
        """Get and Set the height attribute of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    # x getter and setter.
    @property
    def x(self):
        """Get and Set the x attribute of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    # y getter and setter.
    @property
    def y(self):
        """Get and Set the y attribute of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Area of the rectangle."""
        return self.width * self.height

    def display(self):
        """Prints in stdout the Rectangle instance with the character '#'."""
        for i in range(self.height):
            print("#" * self.width)

    def __str__(self):
        """Returns the string representation of the Rectangle."""
        return (
            f"[Rectangle] ({self.id}) {self.x}/{self.y} - "
            f"{self.width}/{self.height}"
        )

    def display(self):
        """Prints in stdout the Rectangle instance with the character '#'."""
        for y_offset in range(self.y):
            print()

        for _ in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def update(self, *args, **kwargs):
        """Updates the attributes of the Rectangle.

        Args:
            *args: Variable number of positional arguments.
                - 1 argument: Updates the id attribute.
                - 2 arguments: Updates the id and width attributes.
                - 3 arguments: Updates the id, width, and height attributes.
                - 4 arguments: Updates the id, width, height, and x attributes.
                - 5 arguments: Updates all attributes.
            **kwargs: Variable number of keyword arguments.
                Each key represents an attribute of the instance.
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle."""
        dictionary = {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
        return dictionary
