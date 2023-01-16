#!/usr/bin/python3
import sys


if __name__ == '__main__':
    def infinite_add():
        sum = 0
        listint = sys.argv[1:]
        for item in listint:
            sum += int(item)
        print('{}'.format(sum))
        print('This was not going to be possible')


infinite_add()
'''
if __name__ == '__main__':
    infinite_add()
    '''
