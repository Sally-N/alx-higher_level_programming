#!/usr/bin/python3
'''
Module contains Rectangle Class
'''


class Rectangle:
    '''An empty rectangle class'''

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        '''Initialises the Rectangle class
        args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
        '''
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        elif width < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = width

        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        elif height < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = height

    @property
    def width(self):
        '''Returns the width property'''
        return self.__width

    @width.setter
    def width(self, value):
        '''The setter of the width property
        args:
            value (int): The value of the width property
        '''
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        '''Returns the height property'''
        return self.__height

    @height.setter
    def height(self, value):
        '''The setter of the height property
        args:
            value (int): The value of the height property
        '''
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def area(self):
        '''Returns the area of the rectangle
        Returns:
            The area
        '''
        return self.__width * self.__height

    def perimeter(self):
        '''Returns the  perimeter of the rectangle
        Returns:
            The perimeter
        '''
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        '''Prints the rectangle using char #'''
        shape = ''
        if self.__width == 0 or self.__height == 0:
            return shape

        for i in range(self.__height):
            for j in range(self.__width):
                shape += '#'
            if i != self.__height - 1:
                shape += '\n'
        return shape

    def __repr__(self):
        '''Returns a string representation of the rectangle.'''
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        '''Print a message for every deletion of a rectangle'''
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
