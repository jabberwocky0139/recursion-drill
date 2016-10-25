# -*- coding: utf-8 -*-

## 基本的にPythonには末尾再帰を最適化する機能はない.  

# n! を末尾再帰で定義
def fact_rec_tail(n, m):
    # 終了条件
    # 蓄積変数を返すようにする
    if n == 0:
        return m
    # 継続条件
    # 蓄積変数に対して仕事をする
    else:
        return fact_rec_tail(n-1, m*n)

# 蓄積変数は初期値に設定(5の0乗は1)
## print(fact_rec_tail(5, 1))


# n*m を末尾再帰で定義
def mul_rec_tail(n, m, l):
    # 終了条件1
    if m == 0:
        return 0
    # 終了条件2
    elif m == 1:
        return l
    # 継続条件
    else:
        return mul_rec_tail(n, m-1, l+n)

# 累積関数の初期値に注意! 今回は第一引数と同じにする
## print(mul_rec_tail(5, 1, 5))


# n + m を末尾再帰で定義
def plus_rec_tail(n, m, l):
    # 終了条件
    if m == 0:
        return l
    # 継続条件
    else:
        return plus_rec_tail(n, m-1, l + 1)

# 累積関数の初期値に注意! 今回は第一引数と同じにする
## print(plus_rec_tail(7, 18, 7))


# n^m を末尾再帰で定義
def power_rec_tail(n, m, l):
    # 基底部
    if m == 0:
        return l
    # 再帰部
    else:
        return power_rec_tail(n, m-1, l*n)

print(power_rec_tail(2, 6, 1))

