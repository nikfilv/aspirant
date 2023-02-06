import numpy as np
from lu import decLU, solveLU


n = 8
A = -np.ones((n, n), 'float')

for i in range(0, n):
    A[i, i] = 1
    A[i, n-1] = 1
    if i < n-1:
        A[i, i+1:n-1] = 0
print('A:')
print(A)

LU = decLU(A)
print('LU:')
print(LU)

f = np.ones((n), 'float')
print('b:')
print(f)


x = solveLU(A, f)
print('x:')
print(x)
