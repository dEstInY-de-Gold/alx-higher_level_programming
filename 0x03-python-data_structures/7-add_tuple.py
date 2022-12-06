#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) >= 2 and len(tuple_b) >= 2:
        a, b = tuple_a[0], tuple_a[1]
        x, y = tuple_b[0], tuple_b[1]

    elif len(tuple_a) < 2 or len(tuple_b) < 2:
        if len(tuple_a) < 1 and len(tuple_b) <= 1:
            a = b = 0
            if len(tuple_b) == 1:
                x = tuple_b[0]
                y = 0
            else:
                x = y = 0
        elif len(tuple_a) <= 1 and len(tuple_b) < 1:
            x = y = 0
            if len(tuple_a) == 1:
                a = tuple_a[0]
                b = 0
            else:
                a = b = 0
        elif len(tuple_a) >= 2 and len(tuple_b) < 2:
            a, b = tuple_a[0], tuple_a[1]
            if len(tuple_b) < 1:
                x = y = 0
            else:
                x = tuple_b[0]
                y = 0
        elif len(tuple_b) >= 2 and len(tuple_a) < 2:
            x, y = tuple_b[0], tuple_b[1]
            if len(tuple_a) < 1:
                a = b = 0
            else:
                a = tuple_a[0]
                b = 0
    added_tuple1 = a + x
    added_tuple2 = b + y
    return (added_tuple1, added_tuple2)
