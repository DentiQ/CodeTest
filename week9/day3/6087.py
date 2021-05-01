from sys import stdin
from collections import deque

input = stdin.readline

W, H = map(int, input().split())

mtrx = [list(input().rstrip()) for _ in range(H)]

visited = [[9999999 for _ in range(W)] for _ in range(H)]

start = tuple()
end = tuple()

flag = True

for i in range(H):
    for j in range(W):
        if mtrx[i][j] == "C" and flag:
            start = (i, j)
            flag = False
        elif mtrx[i][j] == "C" and not flag:
            end = (i, j)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

queue = deque([(start[0], start[1])])
visited[start[0]][start[1]] = 0

while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        while True:
            if nx >= H or nx < 0 or ny >= W or ny < 0:
                break

            if mtrx[nx][ny] == "*":
                break

            if visited[nx][ny] < visited[x][y] + 1:
                break

            queue.append((nx, ny))
            visited[nx][ny] = visited[x][y] + 1
            nx += dx[i]
            ny += dy[i]

print(visited[end[0]][end[1]] - 1)




