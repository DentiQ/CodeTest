from itertools import permutations

k = int(input())
op = input().split()
ans = []

perm = list(permutations([i for i in range(9+1)], k+1))

for num in perm:
    flag = True
    for i in range(k):
        if op[i] == '<':
            if num[i] < num[i+1]:
                continue
            else:
                flag = False
                break
        elif op[i] == '>':
            if num[i] > num[i+1]:
                continue
            else:
                flag = False
                break
    if flag:
        ans.append(num)

print("".join([str(i) for i in ans[-1]]))
print("".join([str(i) for i in ans[0]]))