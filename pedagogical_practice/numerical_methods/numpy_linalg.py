import numpy as np

print('A*x = b')

A = np.matrix([[4, 3, -2], [1, 2, 1], [3, 2, 1]])
print(f'{A=}')
b = np.matrix([4, 8, 10]).transpose()
print(f'{b=}')

x = np.linalg.solve(A, b)
print(f'{x=}')

print(f'{np.dot(A, x)=}')