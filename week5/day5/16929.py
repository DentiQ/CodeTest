from sys import stdin

input = stdin.readline

n, m = map(int, input().split())

game = [[] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]

for i in range(n):
    game[i] = input().strip()

ans = False


def dfs(x, y, sx, sy, cnt):
    global ans
    if ans:
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= n or ny >= m or game[nx][ny] != game[sx][sy]:
            continue

        if not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, sx, sy, cnt+1)
        else:
            if cnt >= 4 and nx == sx and ny == sy:
                ans = True
                return


for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            visited[i][j] = True
            dfs(i, j, i, j, 1)
        if ans:
            print('Yes')
            exit(0)
        visited = [[False] * m for _ in range(n)]

print('No')