#!/usr/bin/python3
import sys
from calculator_1 import add, mul, sub, div, power


def calc():
    args = sys.argv[1:]
    print(args)
    if len(args) != 3:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
    elif args[1] not in ['+', '-', '*', '**', '/']:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)
    else:
        args[0], args[2] = int(args[0]), int(args[2])
        if args[1] == '+':
            res = add(args[0], args[2])
        elif args[1] == '*':
            res = mul(args[0], args[2])
        elif args[1] == '-':
            res = sub(args[0], args[2])
        elif args[1] == '/':
            res = div(args[0], args[2])
        elif args[1] == '**':
            res = power(args[0], args[2])
    '''
    else:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)
    if len(args) != 3:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
        '''
    print('{} {} {} = {}'.format(args[0], args[1], args[2], res))


if __name__ == '__main__':
    calc()
