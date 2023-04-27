#!/usr/bin/python3


def append_write(filename='', text=''):
    '''
    Appends to existing contents of file
    Args:
        filename: file name
        text: content to append
    '''
    with open(filename, 'a', encoding="utf-8") as f:
        f.write(text)
        return len(text)
