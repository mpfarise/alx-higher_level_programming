#!/usr/bin/python3
# 5-no_c.py

def no_c(my_string):
    """Remove all characters c and c from a string"""
    copy = [x for x in my_stringif x != 'c' and x != 'C']
    return ("".join(copy))
