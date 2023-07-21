"""
Напишите функцию для транспонирования матрицы
"""

import numpy as np

matrix = [[1,2,3],[4,5,6]]

def transponision_from_numpy(data):
    arr_matrix = np.array(data)
    result = arr_matrix.transpose()
    return result

print(transponision_from_numpy(matrix))
print()
def transpon_func(list):
    transporate_matrix = [[0 for j in range(len(list))] for i in range(len(list[0]))]

    for i in range(len(list)):
        for j in range(len(list[0])):
            transporate_matrix[j][i] = list[i][j]

    return transporate_matrix

print(transpon_func(matrix))
