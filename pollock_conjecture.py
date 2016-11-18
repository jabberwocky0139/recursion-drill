# coding: utf-8
from collections import deque
import sys


from pprint import pprint
def reg_tetra(n):
    return n * (n + 1) * (n + 2) // 6


def make_reg_tetra(m):
    i, ans, flag = 1, [], reg_tetra(1)    
    while m >= flag:
        i += 1
        ans.append(flag)
        flag = reg_tetra(i)
    return ans


def make_reg_tetra_odd(iter):
    return list(filter(lambda x: x % 2 != 0, iter))

"""
def rec_number(n, iter):
    if dp[len(iter)][n] is not None:
        return dp[len(iter)][n]
    # 終了条件
    elif n == 0:
        return 0
    # 継続条件
    elif len(iter) == 1:
        return n
    else:
        if(n - iter[-1] < 0):
            dp[len(iter)][n] = rec_number(n, iter[:-1])
        else:
            dp[len(iter)][n] = min(rec_number(n - iter[-1], iter) + 1, rec_number(n, iter[:-1]))
        return dp[len(iter)][n]

def new_rec_number(len_iter, n, iter):
    if dp[len_iter][n] is not None:
        return dp[len_iter][n]
    # 終了条件
    elif n == 0:
        return 0
    # 継続条件
    elif len_iter == 1:
        return n
    else:
        if n - iter[len_iter-1] < 0:
            dp[len_iter][n] = new_rec_number(len_iter - 1, n, iter)
        else:
            dp[len_iter][n] = min(new_rec_number(len_iter, n - iter[len_iter-1], iter) + 1, new_rec_number(len_iter - 1, n, iter))
        return dp[len_iter][n]

def wrap_number(dp, n, iter):
    new_rec_number(len(iter), n, iter)
"""

# dp[len_iter][n]
# 1 <= i <= len_iter    0 <= j <= n
def dynamic_number(n, iter):
    len_iter = len(iter)
    for i in range(1, len_iter+1):
        for j in range(n + 1):
            # 終了条件
            if j == 0:
                dp[i][j] = 0
            elif i == 1:
                dp[i][j] = j
            # 継続条件
            else:
                if j - iter[i-1] < 0: ## if n - iter[len_iter-1] < 0:
                    dp[i][j] = dp[i-1][j] ## new_rec_number(len_iter - 1, n, iter)
                else:
                    dp[i][j] = min(dp[i][j-iter[i-1]] + 1, dp[i-1][j]) ## min(new_rec_number(len_iter, n - iter[len_iter-1], iter) + 1, new_rec_number(len_iter - 1, n, iter))

                    
f = open("input2.txt", "r") ## debug
# 標準入力
arr = []
while True:
    # n = int(input())
    n = int(f.readline()) ## debug
    if n == 0:
        break
    arr.append(n)

# arr = [40] ## debug

D = deque
for i in range(181):
    D.append(i*(i+1)*(i+2)//6)
    
def dynamic_number2(n, D):
    for i in range(n):
        for j in D:
            if(i + j <= n):
                dp[i+j] = min(dp[i+j], dp[i]+1)


dp = [i for i in range(1000002)]
dynamic_number2(1000000, D)


for n in arr:
    print(dp[n])
    """
    dp = [i for i in range(n+1)]
    odd = dynamic_number2(n, dp, iter_odd)[-1]
    print(regular, odd)
    """
    
    """
    arr_tetra= make_reg_tetra(n)
    arr_tetra_odd = make_reg_tetra_odd(arr_tetra)

    # sample3
    dp = [[0]*(n+1) for i in range(len(arr_tetra) + 1)]
    dynamic_number(n, arr_tetra)
    a = dp[len(arr_tetra)][n]
    
    dp = [[0]*(n+1) for i in range(len(arr_tetra_odd) + 1)]
    dynamic_number(n, arr_tetra_odd)
    b = dp[len(arr_tetra_odd)][n]
    print(a, b)
    """
    # sample2
    """
    wrap_number(dp, n, arr_tetra)
    a = dp[len(arr_tetra)][n]
    dp = [[None]*(n+1) for i in range(len(arr_tetra) + 1)]
    wrap_number(dp, n, arr_tetra_odd)
    b = dp[len(arr_tetra_odd)][n]
    """
    # sample1
    """
    a = rec_number(n, arr_tetra)
    dp = [[None]*(n+1) for i in range(len(arr_tetra_odd) + 1)]
    b = rec_number(n, arr_tetra_odd)
    """
    
