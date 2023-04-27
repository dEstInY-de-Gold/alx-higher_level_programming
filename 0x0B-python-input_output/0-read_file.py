#!/usr/bin/python3


def read_file(filename=""):
    '''
    Reads contents of file
    Accepts filename as a parameter, opens it and
    prints the output to stout.
    Args:
        filename: given file to read from
    '''
    with open(filename, 'r') as f:
        print(f.read())
