import sys
from random import randint


def sum_rec(arr, m):
    # 終了条件
    if len(arr) == 0:
        return m

    # 継続条件
    return sum_rec(arr[1:], m + arr[0])

    
def product_rec(arr, m):
    # 終了条件
    if len(arr) == 0:
        return m

    # 継続条件
    return product_rec(arr[1:], m * arr[0])

    
def maximum_rec(arr):
    # 終了条件
    if len(arr) == 0:
        sys.exit(-1)
    elif len(arr) == 1:
        return arr[0]

    # 継続条件
    return max(arr[0], maximum_rec(arr[1:]))


def is_true_rec(arr):
    # 終了条件
    if len(arr) == 0:
        return True
    if arr[]

    # 継続条件
    return arr[0] and is_true_rec(arr[1:])


print(is_true_rec([True, False, True]))
