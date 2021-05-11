"""
https://www.acmicpc.net/problem/4963
섬의 개수
정사각형으로 이루어져 있는 섬과 바다 지도가 주어진다. 섬의 개수를 세는 프로그램을 작성하시오.
한 정사각형과 가로, 세로 또는 대각선으로 연결되어 있는 사각형은 걸어갈 수 있는 사각형이다.
두 정사각형이 같은 섬에 있으려면, 한 정사각형에서 다른 정사각형으로 걸어서 갈 수 있는 경로가 있어야 한다.
지도는 바다로 둘러싸여 있으며, 지도 밖으로 나갈 수 없다.

입력
입력은 여러 개의 테스트 케이스로 이루어져 있다.
각 테스트 케이스의 첫째 줄에는 지도의 너비 w와 높이 h가 주어진다.
w와 h는 50보다 작거나 같은 양의 정수이다.
둘째 줄부터 h개 줄에는 지도가 주어진다. 1은 땅, 0은 바다이다.
입력의 마지막 줄에는 0이 두 개 주어진다.

출력
각 테스트 케이스에 대해서, 섬의 개수를 출력한다.
"""

from sys import stdin
from collections import deque

input = stdin.readline

dx = [1, 0, 0, -1, 1, 1, -1, -1]
dy = [0, 1, -1, 0, 1, -1, 1, -1]

while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break

    sea = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False for _ in range(w)] for _ in range(h)]

    ans = 0

    for i in range(w):
        for j in range(h):
            if sea[j][i] == 1 and not visited[j][i]:
                q = deque()
                q.append([j, i])
                ans += 1

                while q:
                    t = q.popleft()
                    x = t[0]
                    y = t[1]
                    for k in range(8):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < h and 0 <= ny < w:
                            if not visited[nx][ny] and sea[nx][ny] == 1:
                                visited[nx][ny] = True
                                q.append([nx, ny])

    print(ans)