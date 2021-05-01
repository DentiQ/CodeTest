from itertools import combinations_with_replacement

N, M = map(int, input().split())

office = [list(map(int, input().split())) for _ in range(N)]

print(office)

dx = [-1, 0, 0, 1]
dy = [0, 1, -1, 0]

cctv_list = []

for i in range(N):
    for j in range(M):
        if 1 <= office[i][j] <= 5:
            cctv_list.append([i, j])


def CCTV(type, pos, direct):
    if type == 1:
        while True:
            print()

print(cctv_list)