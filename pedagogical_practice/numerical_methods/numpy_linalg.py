import numpy as np
import scipy

print('A*x = b')

A = np.array([[4, 3, -2], [1, 2, 1], [3, 2, 1]])
print(f'{A=}')
b = np.array([4, 8, 10]).transpose()
print(f'{b=}')


print('numpy:')
x = np.linalg.solve(A, b)
print(f'{x=}')

print('scipy:')
x = scipy.linalg.solve(A, b)
print(f'{x=}')


print(f'{np.dot(A, x)=}')
