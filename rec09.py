import sys

# 与えられたリストの逆リストを返す
def reverse_rec(arr, m):
    # 終了条件
    if len(arr) == 0:
        return m

    # 継続条件
    m.append(arr[-1])
    return reverse_rec(arr[:-1], m)

## arr = [1, 2, 3, 4, 3, 2, 1, 0]
## print(reverse_rec(arr, []))


def close(string):
    if string[0] is ")":
        return 1
    else:
        print("no close parenthesis")
        sys.exit()

def paren_seq(string):
    if string[0] is "(":
        open_sec(string[1:])
    else:
        return 0

def open_sec(string):
    pass

