from itertools import permutations

N, M = map(int, input().split())

arr = list(map(int, input().split()))

perm = list(permutations(arr, M))

perm.sort()

ans = []

for item in perm:
    flag = True
    if len(ans) == 0:
        ans.append(item)
    elif item != ans[-1]:
        for i in range(len(item)-1):
            if item[i] > item[i+1]:
                flag = False
                break
        if flag:
            ans.append(item)
    else:
        continue

for item in ans:
    for num in item:
        print(num, end=" ")
    print()