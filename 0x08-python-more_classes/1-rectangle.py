#!/usr/bin/python3
'''
Module contains Rectangle Class
'''


class Rectangle:
    '''An empty rectangle class'''
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
        return self._height

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
            self._height = value
