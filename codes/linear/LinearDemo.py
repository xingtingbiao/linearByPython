#!/usr/bin/python3
import numpy as np
from numpy.linalg import inv
from numpy import dot
from numpy import mat
import pandas as pd

if __name__ == '__main__':
    dataSet = pd.read_csv('data.csv')
    # print(dataSet)
    temp = dataSet.iloc[:, 2:5]
    temp['X0'] = 1
    X = temp.iloc[:, [3, 0, 1, 2]]
    # print(X)
    Y = dataSet.iloc[:, 1].values.reshape(150, 1)
    # print(Y)

    # theta = (X'X)^-1X'Y    直接计算
    theta = dot(dot(inv(dot(X.T, X)), X.T), Y)
    print(theta)

    # theta = theta - alpha(theta*X - Y)*X      梯度下降计算
    theta = np.array([1., 1., 1., 1.]).reshape(4, 1)
    alpha = 0.1
    tmp = theta
    X0 = X.iloc[:, 0].values.reshape(150, 1)
    X1 = X.iloc[:, 1].values.reshape(150, 1)
    X2 = X.iloc[:, 2].values.reshape(150, 1)
    X3 = X.iloc[:, 3].values.reshape(150, 1)
    # 注意这里不对Y进行格式化话, 后面计算类型会不匹配
    # Y = Y.values.reshape(150, 1)
    for i in range(10000):
        tmp[0] = theta[0] + np.sum(alpha * (Y - dot(X, theta)) * X0)/150.
        tmp[1] = theta[1] + np.sum(alpha * (Y - dot(X, theta)) * X1)/150.
        tmp[2] = theta[2] + np.sum(alpha * (Y - dot(X, theta)) * X2)/150.
        tmp[3] = theta[3] + np.sum(alpha * (Y - dot(X, theta)) * X3)/150.
        theta = tmp
    print(theta)
    pass
