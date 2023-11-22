#!/usr/bin/python3
""" define a class Square"""


class Square():
    def __init__(self, size=0, position=(0, 0)):
        """Initialize a nw square.

        Args:
            size (int): d sz of d new square.
            position (int, int): The pos of d new square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("sz must be an int")
        elif value < 0:
            raise ValueError("sz must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("pos must be a tuple of 2 postv int")
        self.__position = value

    def area(self):
        return (self.__size * self.__size)

    def my_print(self):
        if self.__size == 0:
            print()
            return
        [print() for x in range(0, self.__position[1])]
        for x in range(self.__size):
            print(" " * self.__position[0], end="")
            for y in range(self.__size):
                print("#", end="")
            print()