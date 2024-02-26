#!/usr/bin/python3
from models.base import Base
    
class Rectangle(Base):
    """Rectangle class, inherits from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize Rectangle instance."""
        super.__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
    
    @property
    def width(self):
        """Getter method for width attribute."""
        return self.__width
    
    @width.setter
    def width(self, value):
        """Setter method for width attribute."""
        self.__width = value
    
    @property
    def height(self):
        """Getter method for height attribute."""
        return self.__height
    
    @height.setter
    def height(self, value):
        """Setter method for height attribute."""
        self.__height = value
    
    @property
    def x(self):
        """Getter method for x attribute."""
        return self.__x
    
    @x.setter
    def x(self, value):
        """Setter method for x attribute."""
        self.__x = value
    
    @property
    def y(self):
        """Getter method for y attribute."""
        return self.__y
    
    @y.setter
    def y(self, value):
        """Setter method for y attribute."""
        self.__y = value
