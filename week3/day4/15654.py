from itertools import combinations

n, m = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()
combis = list(combinations(arr, m))


for combi in combis:
    print(*combi)