n, k = map(int, input().split())
coin = []
ans = 0

for i in range(n):
    coin.append(int(input()))

coin.reverse()

for won in coin:
    if k > 0:
        ans += k // won
        k %= won

print(ans)
