#!/usr/bin/python3


def read_file(filename=""):
    '''
    Reads contents of file
    Args:
        filename: given file to read from
    '''
    with open(filename, 'r') as f:
        print(f.read())
    f.close()
