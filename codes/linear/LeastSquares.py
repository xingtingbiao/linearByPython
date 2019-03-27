#!/usr/bin/python3
import numpy as np
from numpy.linalg import inv
from numpy import dot
from numpy import mat


if __name__ == '__main__':
    # y=2x
    X = mat([1, 2, 3]).reshape(3, 1)
    Y = 2 * X
    # theta = (X'X)^-1X'Y
    theta = dot(dot(inv(dot(X.T, X)), X.T), Y)
    print(theta)
    pass
