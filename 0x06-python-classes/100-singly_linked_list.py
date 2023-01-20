#!/usr/bin/python3

'''
A node object of struct data for a singly linked list
'''


class Node:
    '''
    class node
    data type for linked lists
    '''
    def __init__(self, data, next_node=None):
        '''
        Struct initializer
        Args:
            data (int): Struct data
            next_node (Node): node
        Raises:
            TypeError: raises TypeError if data is not an integer
            or if next_node is not of type node
        '''
        if not isinstance(data, int):
            raise TypeError('data must be an integer')
        else:
            self.data = data
        if not isinstance(next_node, Node):
            raise TypeError('next_node must be a node object')
        else:
            self.next_node = next_node

    @property
    def data(self):
        '''
        Data value for struct
        Args:
            value (int): Struct data
        Raises:
            TypeError: Raises TypeError if data is not integer
        Returns:
            int: protected data
        '''
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        else:
            self.__data = value

    @property
    def next_node(self):
        '''
        Data struct of next node
        Args:
            value (Node): A node data type
        Raises:
            TypeError: raise TypeError if next_node is not type Node
        Returns:
            Node: next_node of type Node
        '''
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node):# or next_node not None:
            raise TypeError('next_node must be a node object')
        else:
            self.__next_node = value


'''
A list object of singly linked list
'''


class SinglyLinkedList(Node):
    '''
    A singly linked list data initializer
    '''
    node = None

    def __init__(self):
        super().__init__(data, next_node)

    def sorted_insert(self, value):
        '''
        Insertion by sorted order of data
        Args:
            values (int): Struct data value
        Returns:
            Node: A pointer to head node of linked list
        '''
        self.value = value
        if self.node is None:
            self.node = Node(self.value)
            self.next_node = None
        else:
            tmp = self.node
            while tmp:
                if tmp.data <= self.value:
                    tmp1 = tmp
                    tmp = self.value
                    tmp.next_node = tmp
                else:
                    tmp = tmp.next_node 
        return self.node
