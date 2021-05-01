import sys

N, M = map(int, input().split())

sys.setrecursionlimit(10000)

tall_arr = [[] for _ in range(N+1)]
short_arr = [[] for _ in range(N+1)]

for _ in range(M):
    x, y = map(int, input().split())
    tall_arr[x].append(y)
    short_arr[y].append(x)


def dfs_tall(i):
    global tall
    visited[i] = 1

    for k in tall_arr[i]:
        if not visited[k]:
            tall += 1
            dfs_tall(k)

    return tall


def dfs_short(i):
    global short
    visited[i] = 1

    for k in short_arr[i]:
        if not visited[k]:
            short += 1
            dfs_short(k)

    return short


cnt = 0

for i in range(1, N+1):
    visited = [0] * (N + 1)
    tall, short = 0, 0

    tall_std = dfs_tall(i)

    visited = [0] * (N + 1)

    short_std = dfs_short(i)

    if tall_std + short_std == N-1:
        cnt += 1

print(cnt)