#!/usr/bin/python3


class Node:
    def __init__(self, data, next_node=None):
        if isinstance(data, int) not True:
            raise TypeError('data must be an integer')
        else:
            self.__data = data
        if next_node != Node:
            raise TypeError('next_node must be a node object')
        else:
            self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if isinstance(value, int) not True:
            raise TypeError('data must be an integer')
        else:
            self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if type(next_node) not Node or next_node not None:
            raise TypeError('next_node must be a node object')
        else:
            self.__next_node = value


class SinglyLinkedList:
    node = Node

    def __init__(self):
        pass

    def sorted_insert(self, value):
        if node is None:
            node = Node(self.value)
            next_node = None
        else:
            tmp = node
            while tmp:
                if tmp >= self.value:
                    tmp1 = tmp
                    tmp = self.value
                    tmp.next_node = tmp
                else:
                    tmp = tmp.next_node
        return node
