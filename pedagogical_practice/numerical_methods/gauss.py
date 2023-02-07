import numpy as np

a = np.array([
    [4, 3, -2], 
    [1, 2, 1], 
    [3, 2, 1]
    ], float)
print(f'{a=}')

b = np.array([[4], [8], [10]])
print(f'{b=}')

A = np.concatenate((a, b), axis=1)
print(f'{A=}')

n = len(A)
print(f'{n=}')

x = np.zeros(n)

for i in range(n):       
    for j in range(i+1, n):
        ratio = A[j][i]/A[i][i]
        for k in range(n+1):
            A[j][k] = A[j][k] - ratio * A[i][k]
            print(A)


x[n-1] = A[n-1][n]/A[n-1][n-1]

for i in range(n-2,-1,-1):
    x[i] = A[i][n]
    
    for j in range(i+1,n):
        x[i] = x[i] - A[i][j]*x[j]
    
    x[i] = x[i]/A[i][i]


print(f'{x=}')

