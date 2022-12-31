#!/usr/bin/python3

'''
A function thaut prints a text with 2 new lines after each of these characters: '.', '?' and ':'
'''


def text_indentation(text):
    '''
    prints with special treatments to indentations
    Args:
        text (str): parameter
    Raises:
        TypeError: raised if text is mot a string
    '''
    if not isinstance(text, str):
        raise TypeError('string must be a string')
    else:
        for char in ['. ', '? ', ': ', ' :', ' : ']:
            if char in text:
