#!/usr/bin/python3
import sys


def infinite_add():
    sum = 0
    listint = sys.argv[1:]
    for item in listint:
        sum += int(item)
    print('{}'.format(sum))


if __name__ == '__main__':
    infinite_add()
