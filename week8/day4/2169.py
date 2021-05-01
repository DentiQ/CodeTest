from sys import stdin

input = stdin.readline

N, M = map(int, input().split())

dp = [[0 for _ in range(M+1)] for _ in range(N+1)]

matrix = [[0 for _ in range(M+1)] for _ in range(N+1)]

temp = [[0 for _ in range(M+2)] for _ in range(2)]

for i in range(1, N+1):
    matrix[i] = [0] + list(map(int, input().split()))

for j in range(1, M+1):
    dp[1][j] += dp[1][j-1] + matrix[1][j]

for i in range(2, N+1):
    temp[0][0] = dp[i-1][1]
    for j in range(1, M+1):
        temp[0][j] = max(dp[i-1][j], temp[0][j-1]) + matrix[i][j]

    temp[1][M+1] = dp[i-1][M]
    for j in range(M, 0, -1):
        temp[1][j] = max(dp[i-1][j], temp[1][j+1]) + matrix[i][j]

    for j in range(1, M+1):
        dp[i][j] = max(temp[0][j], temp[1][j])

print(dp[N][M])


