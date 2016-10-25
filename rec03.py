# -*- coding: utf-8 -*-

# nが偶数ならTrue
def even_rec(n):
    # 基底部1
    if n == 0:
        return True
    # 基底部2
    elif n == 1:
        return False
    # 再帰部
    # 末尾再帰に(たまたま)なってる
    else:
        return even_rec(n-2)

## print(even_rec(1542))

# l > s ならTrueを返す
def it_rec(l, s):
    if l == 0:
        return False
    elif s == 0:
        return True
    else:
        return it_rec(l-1, s-1)

## print(it_rec(3, 3))

# n//mを出力する
def remeinder_rec(n, m):
    # 終了条件
    if n < m:
        return n
    else:
        return remeinder_rec(n - m, m)

print(remeinder_rec(19, 9))

