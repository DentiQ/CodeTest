"""
https://www.acmicpc.net/problem/16956
늑대와 양
크기가 R×C인 목장이 있고, 목장은 1×1 크기의 칸으로 나누어져 있다.
각각의 칸에는 비어있거나, 양 또는 늑대가 있다. 양은 이동하지 않고 위치를 지키고 있고, 늑대는 인접한 칸을 자유롭게 이동할 수 있다.
두 칸이 인접하다는 것은 두 칸이 변을 공유하는 경우이다.
목장에 울타리를 설치해 늑대가 양이 있는 칸으로 갈 수 없게 하려고 한다. 늑대는 울타리가 있는 칸으로는 이동할 수 없다. 울타리를 설치해보자.

입력
첫째 줄에 목장의 크기 R, C가 주어진다.
둘째 줄부터 R개의 줄에 목장의 상태가 주어진다. '.'는 빈 칸, 'S'는 양, 'W'는 늑대이다.

출력
늑대가 양이 있는 칸으로 갈 수 없게 할 수 있다면 첫째 줄에 1을 출력하고, 둘째 줄부터 R개의 줄에 목장의 상태를 출력한다. 울타리는 'D'로 출력한다.
울타리를 어떻게 설치해도 늑대가 양이 있는 칸으로 갈 수 있다면 첫째 줄에 0을 출력한다.
"""

from sys import stdin
from collections import deque

input = stdin.readline

R, C = map(int, input().split())

field = [list(input().rstrip()) for _ in range(R)]

dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]

wolves = []

flag = True

for i in range(R):
    for j in range(C):
        if field[i][j] == 'W':
            wolves.append([i, j])
            for k in range(4):
                ni = i + dx[k]
                nj = j + dy[k]

                if 0 <= ni < R and 0 <= nj < C:
                    if field[ni][nj] == 'S':
                        flag = False
                        break
                    elif field[ni][nj] == '.':
                        field[ni][nj] = 'D'
    if not flag:
        break

if flag:
    print(1)
    for row in field:
        print("".join(row))
else:
    print(0)





