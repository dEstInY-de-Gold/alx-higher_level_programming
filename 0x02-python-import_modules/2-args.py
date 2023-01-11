#!/usr/bin/python3
import sys

def func_args():
    arg = sys.argv[1:]
    l = len(arg)
    cnt = 0
    if l == 0:
        print('{} arguments.'.format(l))
    elif l == 1:
        print('{} argument:'.format(l))
        print('{}: {}'.format(1, arg[0]))
    else:# l > 1:
        print('{} arguments:'.format(l))
        for i in arg:
            print('{}: {}'.format(cnt + 1, i))
            cnt += 1


if __name__ == '__main__':
    func_args()
