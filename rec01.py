# -*- coding: utf-8 -*-

# 1 + 2 + ... + n を再帰で定義
def soap_rec(n):
    # 終了条件
    if n == 0:
        return 0
    # 継続条件
    else:
        return soap_rec(n-1) + n

# n! を再帰で定義
def fact_rec(n):
    # 終了条件
    if n == 0:
        return 1
    # 継続条件
    else:
        return fact_rec(n-1)*n

# n*m を再帰で定義
def mul_rec(n, m):
    # 終了条件1
    if m == 0:
        return 0
    # 終了条件2
    elif m == 1:
        return n
    # 継続条件
    else:
        return mul_rec(n, m-1) + n

# n + m を再帰で定義
def plus_rec(n, m):
    # 終了条件
    if m == 0:
        return n
    # 継続条件
    else:
        return plus_rec(n, m-1) + 1

# n - m を再帰で定義
def minus_rec(n, m):
    # 終了条件
    if m == 0:
        return n
    # 継続条件
    else:
        return minus_rec(n, m-1) - 1

# n^m を再帰で定義
def power_rec(n, m):
    # 終了条件
    if m == 0:
        return 1
    else:
        return power_rec(n, m-1) * n


print(power_rec(3, 4))
