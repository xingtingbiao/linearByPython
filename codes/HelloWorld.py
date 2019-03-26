#!/usr/bin/python3
import random


def hello_world():
    print('hello {}'.format('world'))
    print('你好 {}'.format('世界'))
    pass


def test_random():
    random.seed()
    for i in range(20):
        random_ = random.random() * 10
        print(random_)
        print(round(random_, 2))
    pass


if __name__ == '__main__':
    test_random()
    pass
