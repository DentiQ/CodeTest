N, M = map(int, input().split())

rx, ry, rd = map(int, input().split())

room = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

ans = 0

while True:
    cnt = 0
    go = False

    if room[rx][ry] == 0:
        room[rx][ry] = -1
        ans += 1

    while cnt < 4:
        rd = (rd + 3) % 4
        nx, ny = rx + dx[rd], ry + dy[rd]
        if room[nx][ny] == 0:
            rx, ry = nx, ny
            go = True
            break
        cnt += 1

    if not go:
        bx, by = rx - dx[rd], ry - dy[rd]
        if room[bx][by] == -1:
            rx, ry = bx, by
        else:
            break

print(ans)