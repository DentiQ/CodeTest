from sys import stdin

input = stdin.readline

N, M = map(int, input().split())

trees = list(map(int, input().split()))

trees.sort()

low = 1
high = trees[-1]

ans = 0

while low <= high:
    temp = 0
    mid = (low + high) // 2
    for tree in trees:
        if tree > mid:
            temp += tree - mid

    if temp < M:
        high = mid - 1
    else:
        low = mid + 1
        ans = mid

print(ans)
