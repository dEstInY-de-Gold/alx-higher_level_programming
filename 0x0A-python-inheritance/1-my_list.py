#!/usr/bin/python3
'''
My list printer
'''

class MyList(list):
    '''
    Prints list in ascending order
    '''
    def __init__(self):
        self.sort()

    def print_sorted(self):
        print(self.sort())
