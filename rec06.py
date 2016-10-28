# -*- coding: utf-8 -*-
from functools import reduce

# (0, 0)から(x, y)までの経路の総数を出力する
def maze(x, y):
    if x == 0 and y == 0:
        return 1
    elif x > 0 and y > 0:
        return maze(x-1, y) + maze(x, y-1)
    elif x > 0 and y == 0:
        return maze(x-1, y)
    elif y > 0 and x == 0:
        return maze(x, y-1)

def half_maze(x, y):
    if x == 0 and y == 0:
        return 1
    elif x == y:
        return maze(x, y-1)
    elif x > 0 and y > 0:
        return maze(x-1, y) + maze(x, y-1)
    elif x > 0 and y == 0:
        return maze(x-1, y)

## print(half_maze(13, 13))

# n個のノードを持つ二分木の総数
def node(n):
    if n == 0:
        return 1
    else:
        return sum([node(i) * node(n-i-1) for i in range(0, n)])

## print(node(3))

def coin(n, arr):
    if n == 0:
        return 1
    elif len(arr) == 0:
        return 0
    elif n < 0:
        return 0
    else:
        return coin(n - arr[0], arr) + coin(n, arr[1:])

print(coin(100, [1, 5, 10, 100, 500]))
