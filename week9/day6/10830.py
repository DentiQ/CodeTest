import sys

sys.setrecursionlimit(100000)

N, B = map(int, input().split())


def mat_pow(x, b):
    if b == 1:
        return x
    if b == 2:
        return mat_mul(x, x)
    elif b % 2 == 0:
        return mat_pow(mat_pow(x, b//2), 2)
    elif b % 2 == 1:
        return mat_mul(x, mat_pow(x, b-1))


def mat_mul(x, y):
    c = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                c[i][j] += (x[i][k] * y[k][j])
            c[i][j] %= 1000

    return c


A = [list(map(int, input().split())) for _ in range(N)]

C = mat_pow(A, B)

for i in range(N):
    for j in range(N):
        C[i][j] %= 1000

for arr in C:
    print(*arr)