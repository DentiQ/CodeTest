T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    plane = [[0 for _ in range(N)] for _ in range(N)]
    for _ in range(M):
        i, j = map(int, input().split())
        plane[i-1][j-1] = 1

    print(N-1)