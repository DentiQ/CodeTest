from itertools import product

n, m = map(int, input().split())

prd = list(product([i for i in range(1, n+1)], repeat=m))

for num in prd:
    print(*num)