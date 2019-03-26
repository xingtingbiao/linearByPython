#!/usr/bin/python3
import random


def Y(X1, X2, X3):
    return 0.65 * X1 + 0.70 * X2 - 0.55 * X3 + 1.95
    pass


def producer():
    fileName = 'data.csv'
    with open(fileName, 'w') as file:
        file.write('Unnamed: 0,Y,X1,X2,X3\n')
        for i in range(150):
            random.seed()
            x1 = round(random.random() * 10, 1)
            x2 = round(random.random() * 6, 1)
            x3 = round(random.random() * 2, 1)
            y = round(Y(x1, x2, x3), 1)
            try:
                file.write(str(i) + ',' + str(y) + ',' + str(x1) + ',' + str(x2) + ',' + str(x3) + '\n')
            except Exception as e:
                print('Write Error')
                print(str(e))
    pass


producer()
