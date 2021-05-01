from itertools import permutations

N, M = map(int, input().split())

arr = list(map(int, input().split()))

perm = list(permutations(arr, M))

perm.sort()

ans = []

for item in perm:
    if len(ans) == 0:
        ans.append(item)
    elif item != ans[-1]:
        ans.append(item)
    else:
        continue

for item in ans:
    for num in item:
        print(num, end=" ")
    print()


