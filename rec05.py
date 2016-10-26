# -*- coding: utf-8 -*-

# aとbの最大公約数を求める(a > b を仮定)
def gcd_rec(a, b):
    if b == 0:
        return a
    elif a - b >= b:
        return gcd_rec(a-b, b)
    else:
        return gcd_rec(b, a-b)

def gcd_rec_fast(a, b):
    if b == 0:
        return a
    else:
        return gcd_rec_fast(b, a%b)

# aとbの最大公倍数を求める(a > b を仮定)
def lcm_rec_fast(a, b):
    return a * b // gcd_rec_fast(a, b)

# fibonacci数列を求める末尾再帰版. 基底部が2つあるので累積変数も2つ.
# 基底部では累積変数を返すようにする. 
def fib_rec_tail(n, m, l):
    if n == 0:
        return l
    elif n == 1:
        return m
    else:
        return fib_rec_tail(n-1, l+m, m)

## print(fib_rec_tail(14, 1, 0))

# even_rec と odd_rec の相互再帰(どちらの基底部もTrueを返すようにするとき)
def even_rec(n):
    # 基底部1
    if n == 0:
        return True
    else:
        return odd_rec(n-1)

def odd_rec(n):
    # 基底部1
    if n == 1:
        return True
    else:
        return not even_rec(n)

print(even_rec(2))



