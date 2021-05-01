from itertools import product

N, M = map(int, input().split())

arr = sorted(list(set(map(int, input().split()))))

ans = list(product(arr, repeat=M))

for i in ans:
    print(*i)