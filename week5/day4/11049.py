import heapq

n = int(input())

arr_vol = []

arr_mul = [[0] * n for _ in range(n)]

for _ in range(n):
    arr_vol.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(n-i):
        x = i + j
        arr_mul[j][x] = 2**32
        for k in range(j, x):
            arr_mul[j][x] = min(arr_mul[j][x], arr_mul[j][k] + arr_mul[k+1][x] + arr_vol[j][0]*arr_vol[k][1]*arr_vol[x][1])

print(arr_mul[0][n-1])


