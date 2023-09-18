#!/usr/bin/python3
"""
User class
"""


class User():
    """ Defines a class - User """

    def __init__(self):
        """ Initializes private email atrribute """
        self.__email = ''

    @property
    def email(self):
        """ Gets value of email attribute """
        return self.__email
    
    @email.setter
    def email(self, value):
        """ Sets the value of email attribute """
        if type(value) is not str:
            raise TypeError("email must be a string")
        self.__email = value


if __name__ == "__main__":

    u = User()
    u.email = "john@snow.com"
    print(u.email)
