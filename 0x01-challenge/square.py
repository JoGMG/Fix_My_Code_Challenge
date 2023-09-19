#!/usr/bin/python3
"""
Square class
"""


class Square():
    """
    Defines a class - Square
    - Attributes:
        -   width:  width of square
        -   height: height of square
    """
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ Sets Square attributes with values"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Returns Area of Square """
        return self.width * self.height

    def PerimeterOfMySquare(self):
        """ Returns Perimeter of Square """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ Returns the String representation of Square """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PerimeterOfMySquare())
