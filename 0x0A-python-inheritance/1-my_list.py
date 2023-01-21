#!/usr/bin/python3
'''
My list printer
'''


class MyList(list):
    '''
    Prints list in ascending order
    '''
    def __init__(self):
        super().__init__()

    def print_sorted(self):
        super().sort()
        print(self.sort())
