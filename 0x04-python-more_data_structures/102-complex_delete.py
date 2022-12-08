#!/usr/bin/python3


def complex_delete(a_dictionary, value):
    dic = a_dictionary
    for key in dic:
        map(lambda dic[key]: del dic[key], if key in dic.items())
'''
        if a_dictionary[key] == value and key in a_ditionary:
            del a_dictionary[key]
            '''
    return a_dictionary
