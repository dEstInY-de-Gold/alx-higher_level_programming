#!/usr/bin/python3
import dis
import hidden_4.pyc


list_names = dis.dis(hidden_4.pyc)


list_names.sort()

for name in list_names:
    print('{}'.format(name))
