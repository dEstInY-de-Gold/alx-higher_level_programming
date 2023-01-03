#!/usr/bin/python3

'''
A function for matrix divition
'''


def matrix_divided(matrix, div):
    '''
    matrix divider
    Args:
        matrix (list of list of ints/floats): tha matrix parameter
        div (int / float): The denumerator for division
    Returns:
        matrix: the newly generated matrix
    '''
    new_mat = []
    flen = len(matrix[0])
    element_error = 'matrix must be a matrix (list of lists) of integers/floats'
    if div == 0:
        raise ZeroDivisionError('division by zero')
    for i in matrix:
        if len(i) != flen:
            raise TypeError('Each row of the matrix must have the same size')
        new_mat.append(i)
        for j in i:
            if type(j) is not int and type(j) is not float:# not isinstance(j, int) or not isinstance(j, float):
                raise TypeError(element_error)
        else:
            if type(div) is not int and type(div) is not float:
                raise TypeError('div must be a number')
            elem = list(map(lambda j: float('{:.2f}'.format(j / div)), i))
            new_mat.append(elem)
            new_mat.remove(new_mat[-2])
    return new_mat
