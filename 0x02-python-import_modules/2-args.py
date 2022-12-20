#!/usr/bin/python3
import sys

def func_args():
    arg = sys.argv[1:]
    l = len(arg)
    if l == 0:
        print('{} arguments.'.format(l))
    elif l == 1:
        print('{} argument:'.format(l))
        print('{} : {}'.format(1, arg[0]))
    elif l > 1:
        print('{} arguments:'.format(l))
        for i in arg:
            print('{} : {}'.format(arg.index(i) + 1, i))


if __name__ == '__main__':
    func_args()
