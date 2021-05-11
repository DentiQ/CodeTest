from sys import stdin

input = stdin.readline

M, N = map(int, input().split())

mat = [list(map(int, input().split())) for _ in range(M)]

dp = [[-1 for _ in range(N)] for _ in range(M)]


dx = [-1, 0, 0, 1]
dy = [0, 1, -1, 0]


def dfs(x, y):
    if x == 0 and y == 0:
        return 1

    if dp[x][y] == -1:
        dp[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if mat[x][y] < mat[nx][ny]:
                    dp[x][y] += dfs(nx, ny)

    return dp[x][y]

print(dfs(M-1, N-1))


