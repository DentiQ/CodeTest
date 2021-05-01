from itertools import combinations

N = int(input())

table = [[0, 0]]

for _ in range(N):
    t, p = map(int, input().split())
    table.append([t, p])

ans = 0

combis = []

for i in range(1, N+1):
    combis += list(combinations(range(1, N+1), i))

for combi in combis:
    time = 1
    cost = 0
    for index in combi:
        if time <= index:
            time = index
            if time + table[index][0] <= N+1:
                time += table[index][0]
                cost += table[index][1]
        else:
            break
    if cost == 75:
        print(combi)
    ans = max(ans, cost)

print(ans)
