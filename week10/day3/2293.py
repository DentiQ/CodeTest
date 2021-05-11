from sys import stdin

input = stdin.readline

n, k = map(int, input().split())

coins = []

dp = [0 for _ in range(k)]
dp[0] = 1

for i in range(n):
    coins.append(int(input()))

for i in range(n):
    for j in range(k):
        break

