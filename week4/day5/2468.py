import sys

sys.setrecursionlimit(10000)

input = sys.stdin.readline

n = int(input())

matrix = [] * n

direct_x = [-1, 1, 0, 0]
direct_y = [0, 0, 1, -1]


def dfs(x, y, rain):
    for direct in range(4):
        go_x = x + direct_x[direct]
        go_y = y + direct_y[direct]

        if (0 <= go_x < n) and (0 <= go_y < n) and not visited[go_x][go_y] and matrix[go_x][go_y] > rain:
            visited[go_x][go_y] = True
            dfs(go_x, go_y, rain)


for _ in range(n):
    matrix.append(list(map(int, input().split())))

matrix_max = max(map(max, matrix))

ans = 1

for rain in range(1, matrix_max):

    visited = [[False]*n for _ in range(n)]
    safe_zone = 0

    for i in range(n):
        for j in range(n):
            if matrix[i][j] > rain and not visited[i][j]:
                safe_zone += 1
                visited[i][j] = True
                dfs(i, j, rain)
    ans = max(safe_zone, ans)

print(ans)