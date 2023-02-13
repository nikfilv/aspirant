import numpy as np
import scipy


def get_task_condition(number_task: int) -> (np.array, np.array):

    if number_task == 1:
        # Task 1
        print('--- Task 1 ---')

        A = np.array([
            [7, 1, 1, 0],
            [1, 5, 2, 1],
            [2, 3, 3, 3],
            [3, 4, 5, 5],
        ])
        print(f'{A=}')

        b = np.array([7, 0, -1, -2]).transpose()
        print(f'{b=}')

    elif number_task == 2:
        # Task 2
        print('--- Task 2 ---')

        A = np.array([
            [4, -6, 0, 8, 0, 0],
            [-6, 8, -12, 0, 16, 0],
            [0, -12, 16, 0, 0, 0],
            [8, 0, 0, 20, -8, 0],
            [0, 16, 0, -8, 24, -8],
            [0, 0, 10, 0, -8, 24],
        ])
        print(f'{A=}')

        b = np.array([24, 54, 84, 48, 72, 158]).transpose()
        print(f'{b=}')

    elif number_task == 3:
        # Task 3
        print('--- Task 3 ---')

        n = 4

        A = np.zeros([n, n])
        for idx, x in np.ndenumerate(A):
            if idx[0] == idx[1]:
                A[idx] = 2
            if abs(idx[0] - idx[1]) == 1:
                A[idx] = -1

        print(f'{A=}')

        b = np.zeros(n)
        b[0] = 1
        b[n-1] = -1
        b = b.transpose()
        print(f'{b=}')

    else:
        raise Exception('Task empty')

    return A, b


A, b = get_task_condition(1)

x = np.linalg.solve(A, b)
print(f'{x=}')
# print(f'{np.dot(A, x)=}')


"""LU"""
lu, piv = scipy.linalg.lu_factor(A)
print(f'{lu=}')
# print(f'{piv=}')

x = scipy.linalg.lu_solve((lu, piv), b)
print(f'{x=}')

"""QR"""
q, r = scipy.linalg.qr(A)
print(f'{q=}')
print(f'{r=}')


"""Cholesky"""

c, lower = scipy.linalg.cho_factor(A)
print(f'{c=}')
# print(f'{lower=}')

x = scipy.linalg.cho_solve((c, lower), b)
print(f'{x=}')