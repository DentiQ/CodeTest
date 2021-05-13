"""
https://www.acmicpc.net/problem/7562
나이트의 이동
문제
체스판 위에 한 나이트가 놓여져 있다. 나이트가 한 번에 이동할 수 있는 칸은 아래 그림에 나와있다.
나이트가 이동하려고 하는 칸이 주어진다. 나이트는 몇 번 움직이면 이 칸으로 이동할 수 있을까?

입력
입력의 첫째 줄에는 테스트 케이스의 개수가 주어진다.
각 테스트 케이스는 세 줄로 이루어져 있다. 첫째 줄에는 체스판의 한 변의 길이 l(4 ≤ l ≤ 300)이 주어진다.
체스판의 크기는 l × l이다. 체스판의 각 칸은 두 수의 쌍 {0, ..., l-1} × {0, ..., l-1}로 나타낼 수 있다.
둘째 줄과 셋째 줄에는 나이트가 현재 있는 칸, 나이트가 이동하려고 하는 칸이 주어진다.

출력
각 테스트 케이스마다 나이트가 최소 몇 번만에 이동할 수 있는지 출력한다.
"""
from sys import stdin
from collections import deque

input = stdin.readline

T = int(input())

dx = [-2, -1, 1, 2, -2, -1, 1, 2]
dy = [1, 2, -2, -1, -1, -2, 2, 1]

for _ in range(T):
    L = int(input())

    chess = [[0 for _ in range(L)] for _ in range(L)]

    sx, sy = map(int, input().split())
    gx, gy = map(int, input().split())

    q = deque()

    chess[sy][sx] = 0

    q.append((sx, sy))

    flag = True

    while q:
        x, y = q.popleft()
        if x == gx and y == gy:
            print(chess[gy][gx])
            break
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < L and 0 <= ny < L and chess[ny][nx] == 0:
                q.append((nx, ny))
                chess[ny][nx] = chess[y][x] + 1