from itertools import permutations

n = int(input())
combi = list(permutations([i for i in range(1, n+1)], n))

for i in combi:
    print(*i, sep=" ")
