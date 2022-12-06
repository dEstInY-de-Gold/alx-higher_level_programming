#!/usr/bin/python3

def no_c(my_string):
    for ch in string:
        if ch in 'Cc':
            continue
        else:
            new_string += ch
#    new_string = my_string.translate({ord('c'): None, ord('C'): None})
    return new_string
