#!/usr/bin/python3


def write_file(filename="", text=""):
    '''
    Overwrites contents of a file
    Args:
        filename: filename
        text: content to write into file
    '''
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
    f.close()
