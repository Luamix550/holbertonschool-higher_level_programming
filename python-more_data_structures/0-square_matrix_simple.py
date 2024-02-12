#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared_matrix_simple = [[element**2 for element in row] for row in matrix]
    return squared_matrix_simple
    result = square_matrix_simple()
    print(result)
