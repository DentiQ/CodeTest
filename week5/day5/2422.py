from sys import stdin

input = stdin.readline

N, M = map(int, input().split())

if N <= 2:
    print(0)

else:
    no_combis = {i: [] for i in range(1, N + 1)}
    for _ in range(M):
        x, y = map(int, input().split())
        no_combis[x].append(y)
        no_combis[y].append(x)

    ans = 0

    for i in range(1, N+1):
        for j in range(i+1, N+1):
            if j in no_combis[i]:
                continue
            for k in range(j+1, N+1):
                if k in no_combis[j] or k in no_combis[i]:
                    continue
                ans += 1

    print(ans)
