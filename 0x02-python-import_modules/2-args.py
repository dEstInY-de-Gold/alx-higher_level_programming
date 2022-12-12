#!/usr/bin/python3
<<<<<<< HEAD


def func_args(**arg):
    l = len(arg)
    if l == 0:
        print('{} arguments.'.format(l))
    elif l == 1:
        print('{} argument:'.format(l))
        print('{} : {}'.format(1, arg[0]))
    elif l > 1:
        print('{} arguments:')
        for i in arg:
            print('{} : {}'.format(arg.index(i), i))


func_args()
=======
import sys

if __name__ == '__main__':
    argvs = sys.argv[:]

>>>>>>> c7bf212 (argv in py)
