from sys import stdin
from collections import deque

Input = stdin.readline

N, M = map(int, Input().split())

tmt = [list(map(int, Input().split())) for _ in range(M)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

day = -1

queue = deque()

for i in range(M):
    for j in range(N):
        if tmt[i][j] == 1:
            queue.append((i, j))

while queue:
    day += 1

    for _ in range(len(queue)):
        x, y = queue.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx < 0 or nx >= M or ny < 0 or ny >= N or tmt[nx][ny] in [1, -1]:
                continue

            queue.append((nx, ny))
            tmt[nx][ny] = 1

for arr in tmt:
    if 0 in arr:
        print(-1)
        exit()

print(day)



