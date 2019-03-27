#!/usr/bin/python3
import numpy as np
from numpy.linalg import inv
from numpy import dot
from numpy import mat


if __name__ == '__main__':
    # reshape转换, 相对.T更为灵活
    a = np.arange(15).reshape(3, 5)
    print('a:\n', a)
    A = mat([1, 1])
    AA = np.array([1, 1])
    print('A:\n', A)
    print('AA:\n', AA)
    B = mat([[1, 2], [2, 3]])
    print('B:\n', B)
    print('B的逆:\n', inv(B))
    # 单独取某一行
    print('B的第一行:\n', B[0, :])
    # 某一列
    print('B的第一列:\n', B[:, 0])

    # A: 1*2  B: 2*2
    print('A.B:\n', dot(A, B))
    print('B.AT:\n', dot(B, A.T))
    pass
