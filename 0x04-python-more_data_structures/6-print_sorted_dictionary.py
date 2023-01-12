#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    listed_thensort = list(a_dictionary.keys())
    listed_thensort.sort()
    for i in listed_thensort:
        print("{}: {}".format(i, a_dictionary.get(i)))
