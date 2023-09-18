#!/usr/bin/python3
""" Square class """


class Square:
    """ Defines a class - Square """
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ Initializes Square class attributes """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Returns the area of Square """
        return self.width * self.height

    def PerimeterOfMySquare(self):
        """ Returns the perimeter of Square """
        return 2 * (self.width + self.height)

    def __str__(self):
        """ Returns the String representation of Square """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PerimeterOfMySquare())
