from sys import stdin

input = stdin.readline

n = int(input())

A = [[] for _ in range(n)]

for i in range(n):
    A[i] = list(map(int, input().split()))

#     좌 하 우 상
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

x, y = n // 2, n // 2
ans, di, cnt, move, turn = 0, 0, 0, 0, 1


def move_sand(x, y, sand):
    global ans

    if 0 <= x < n and 0 <= y < n:
        A[x][y] += sand
    else:
        ans += sand


while True:
    nx = x + dx[di]
    ny = y + dy[di]

    if A[nx][ny]:
        per_1 = int(A[nx][ny] * 0.01)
        per_2 = int(A[nx][ny] * 0.02)
        per_5 = int(A[nx][ny] * 0.05)
        per_7 = int(A[nx][ny] * 0.07)
        per_10 = int(A[nx][ny] * 0.1)
        next_sand = A[nx][ny] - 2 * (per_1 + per_2 + per_7 + per_10) - per_5

        per_1_x0, per_1_y0 = nx + dx[(di + 3) % 4], ny + dy[(di + 3) % 4]
        per_1_x1, per_1_y1 = nx + dx[(di + 1) % 4], ny + dy[(di + 1) % 4]
        per_2_x0, per_2_y0 = nx + 2 * dx[(di + 3) % 4], ny + 2 * dy[(di + 3) % 4]
        per_2_x1, per_2_y1 = nx + 2 * dx[(di + 1) % 4], ny + 2 * dy[(di + 1) % 4]
        per_7_x0, per_7_y0 = nx + dx[(di + 3) % 4], ny + dy[(di + 3) % 4]
        per_7_x1, per_7_y1 = nx + dx[(di + 1) % 4], ny + dy[(di + 1) % 4]

        tempx, tempy = nx + dx[di], ny + dy[di]
        per_10_x0, per_10_y0 = tempx + dx[(di + 3) % 4], tempy + dy[(di + 3) % 4]
        per_10_x1, per_10_y1 = tempx + dx[(di + 1) % 4], tempy + dy[(di + 1) % 4]
        per_5_x, per_5_y = tempx + dx[di], tempy + dy[di]
        queue = [[tempx, tempy, next_sand], [per_1_x0, per_1_y0, per_1], [per_1_x1, per_1_y1, per_1],
                 [per_2_x0, per_2_y0, per_2], [per_2_x1, per_2_y1, per_2], [per_7_x0, per_7_y0, per_7],
                 [per_7_x1, per_7_y1, per_7], [per_10_x0, per_10_y0, per_10], [per_10_x1, per_10_y1, per_10],
                 [per_5_x, per_5_y, per_5]]

        for ix, iy, isand in queue:
            move_sand(ix, iy, isand)

    if x == 0 and y == 0:
        break

    A[nx][ny] = 0
    x, y = nx, ny
    cnt += 1
    if cnt == turn:
        di = (di + 1) % 4
        cnt = 0
        move += 1
        if move % 2 == 0:
            turn += 1
            move = 0

print(ans)
