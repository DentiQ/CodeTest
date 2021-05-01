n = input()

ans = 0

for i in range(1, len(n)):
    ans += i * 9 * 10**(i-1)

ans += (int(n) - 10**(len(n)-1) + 1)*len(n)

print(ans)
"""
1 ~ 9 : 1 * 9 - (1 * 9 * 10^0)
10 ~ 99 : 2 * 90 - (2 * 9 * 10^1)
100 ~ 999 : 3 * 900

"""