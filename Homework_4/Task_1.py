""" Задача №1
Напишите функцию для транспонирования матрицы.
"""


def transpose_matrix(matrix_to_transpose):
    rows = len(matrix_to_transpose)
    cols = len(matrix_to_transpose[0])

    transposed_matrix = [[0 for _ in range(rows)] for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            transposed_matrix[j][i] = matrix_to_transpose[i][j]

    return matrix_to_transpose, transposed_matrix


matrix1 = [[7, 11], [3, 4], [99, -2]]
original_matrix, transposed_matrix = transpose_matrix(matrix1)

print("Исходная матрица:")
for row in original_matrix:
    print(row)

print("Транспонированная матрица:")
for row in transposed_matrix:
    print(row)
