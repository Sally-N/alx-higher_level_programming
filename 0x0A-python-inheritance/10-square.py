#!/usr/bin/python3
'''
Module contains class Square
'''

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''
    A square class
    '''
    def __init__(self, size):
        '''
        args:
            size (int): Size of a square side
        '''
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        '''
        Returns area of the Square instance
        '''
        return self.__size ** 2
