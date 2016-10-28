memo = [None]*10000
memo2 = [[None]*10000 for j in range(1000)]


# フィボナッチのメモ化版
def fib_memo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif memo[n] is not None:
        return memo[n]
    else:
        memo[n] = fib_memo(n-1) + fib_memo(n-2)
        return memo[n]

## print(fib_memo(500))

# (0, 0)から(x, y)までの経路の総数を出力するやつのメモ化
def maze(x, y):
    # 終了条件
    if x == 0 and y == 0:
        return 1

    # メモ化
    if memo2[x-1][y] is None and x > 0:
        memo2[x-1][y] = maze(x-1, y)
    if memo2[x][y-1] is None and y > 0:
        memo2[x][y-1] = maze(x, y-1)

    # 継続条件
    if x > 0 and y > 0:
        return memo2[x-1][y] + memo2[x][y-1]
    elif x > 0 and y == 0:
        return memo2[x-1][y]
    elif y > 0 and x == 0:
        return memo2[x][y-1]

## print(maze(6, 6))


# ノードの個数のメモ化版
def node(n):
    # 終了条件
    if n == 0:
        return 1

    # メモ化
    for i in range(0, n):
        if memo[i] is None:
            memo[i] = node(i)
        if memo[n-i-1] is None:
            memo[n-i-1] = node(n-i-1)

    # 継続条件
    return sum([memo[i] * memo[n-i-1] for i in range(0, n)])

## print(node(13))

# arr = [1, 5, 10, 50, 100, 500]が初期値
def coin(n, arr):
    # 終了条件1 : 0円は1通り
    if n == 0:
        return 1
    # 終了条件2 : 使える硬貨がなくなったら終了
    elif len(arr) == 0:
        return 0
    # 終了条件3 : その硬貨では両替できない
    elif n < 0:
        return 0

    # メモ化
    if memo2[n][len(arr)] is None:
        memo2[n][len(arr)] = coin(n - arr[0], arr) + coin(n, arr[1:])

    # 継続条件
    return memo2[n][len(arr)]


print(coin(500, [1, 5, 10, 50, 100, 500]))
