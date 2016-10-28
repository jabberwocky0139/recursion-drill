memo = [0 for i in range(10000)]
memo2 = [[0 for i in range(1000)] for j in range(1000)]

# フィボナッチのメモ化版
def fib_memo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif memo[n] != 0:
        return memo[n]
    else:
        memo[n] = fib_memo(n-1) + fib_memo(n-2)
        return memo[n]

## print(fib_memo(500))

# (0, 0)から(x, y)までの経路の総数を出力するやつのメモ化
def maze(x, y):
    if x == 0 and y == 0:
        return 1
    elif x > 0 and y > 0:
        return maze(x-1, y) + maze(x, y-1)
    elif x > 0 and y == 0:
        return maze(x-1, y)
    elif y > 0 and x == 0:
        return maze(x, y-1)


# ノードの個数のメモ化版
def node(n):
    if n == 0:
        return 1
    elif memo[]:
        return sum([node(i) * node(n-i-1) for i in range(0, n)])
    





