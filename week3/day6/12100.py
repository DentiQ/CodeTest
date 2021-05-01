import sys
from itertools import product
import copy

input = sys.stdin.readline

n = int(input())

arr = [] * n

for i in range(n):
    arr.append(list(map(int, input().split())))

prod = list(product(['up', 'down', 'left', 'right'], repeat=5))

ans = 0


def rotate_90():
    result = copy.deepcopy(arr)

    for r in range(n):
        for c in range(n):
            result[c][n-1-r] = arr[r][c]
    return result


def rotate_180():
    result = copy.deepcopy(arr)

    for r in range(n):
        for c in range(n):
            result[n-1-r][n-1-c] = arr[r][c]
    return result


def rotate_270():
    result = copy.deepcopy(arr)

    for r in range(n):
        for c in range(n):
            result[n-1-c][r] = arr[r][c]
    return result


def move_left():
    for i in range(n):
        p = 0
        x = 0
        for q in range(n):
            if arr[i][q] == 0: continue
            if x == 0:
                x = arr[i][q]
            else:
                if x == arr[i][q]:
                    arr[i][p] = 2 * x
                    p = p + 1
                    x = 0
                else:
                    arr[i][p] = x
                    p = p + 1
                    x = arr[i][q]
            arr[i][q] = 0
        if x != 0: arr[i][p] = x
    return arr


for case in prod:
    for move in case:
        if move == 'up':
            arr = rotate_270()
            move_left()
            arr = rotate_90()
        elif move == 'down':
            arr = rotate_90()
            move_left()
            arr = rotate_270()
        elif move == 'left':
            move_left()
        elif move == 'right':
            arr = rotate_180()
            move_left()
            arr = rotate_180()

    ans = max(ans, max(map(max, arr)))

print(ans)

