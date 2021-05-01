from itertools import permutations

n = int(input())

ans = list(map(int, input().split()))

flag = True
try:
    i = n - 1

    while i > 0 and ans[i - 1] >= ans[i]:
        i -= 1

    if i == 0:
        flag = False

    j = n - 1

    while ans[i - 1] >= ans[j]:
        j -= 1

    ans[i - 1], ans[j] = ans[j], ans[i - 1]

    j = n - 1

    while i < j:
        ans[i], ans[j] = ans[j], ans[i]
        i += 1
        j -= 1

    if flag:
        print(*ans)
    else:
        print(-1)
except IndexError:
    print(-1)
