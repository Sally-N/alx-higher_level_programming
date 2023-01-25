#!/usr/bin/python3

def safe_print_division(a, b):
    '''
    Divides 2 integers and prints the result
    '''
    try:
        ans = a / b
    except (ZeroDivisionError, TypeError):
        pass
    finally:
        print('Inside result: {}'.format(ans))
        return ans
