#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    mutliplied_dictionary = {}
    for key in a_dictionary:
        mutliplied_dictionary[key] = a_dictionary[key] * 2

    return mutliplied_dictionary
