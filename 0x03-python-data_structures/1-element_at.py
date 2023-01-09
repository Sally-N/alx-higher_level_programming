#!/usr/bin/python3
def element_at(my_list, idx):
    position = 0
    if idx < 0 or idx > len(my_list):
        return None
    for number in my_list:
        if position == idx:
            return i
        position += 1
