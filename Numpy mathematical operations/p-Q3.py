import numpy as np
matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])
# Matrix multiplication
result_matmul = np.dot(matrix_a, matrix_b)
# Matrix transposition
result_transpose = np.transpose(matrix_a)
print("Matrix Multiplication:")
print(result_matmul)
print("Original Matrix :")
print(matrix_a)
print("After Matrix Transposition:")
print(result_transpose)