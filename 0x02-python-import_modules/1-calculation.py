#!/usr/bin/python3
import calculator_1 as calc

if __name__ == '__main__':
    a = 10
    b = 5
    add = calc.add(a, b)
    sub = calc.sub(a, b)
    mul = calc.mul(a, b)
    div = calc.div(a, b)
    print('{} + {} = {}'.format(a, b, add))
    print('{} - {} = {}'.format(a, b, sub))
    print('{} * {} = {}'.format(a, b, mul))
    print('{} / {} = {}'.format(a, b, div))