from sys import stdin

input = stdin.readline

N = int(input())

nums = list(map(int, input().split()))

ans = [[0] * N for _ in range(N)]

for i in range(N):
    ans[i][i] = 1

for i in range(N-1):
    if nums[i] == nums[i+1]:
        ans[i][i+1] = 1

for i in range(N):
    for start in range(N):
        end = start + i
        if end >= N:
            break
        if start == end or start + 1 == end:
            continue
        if nums[start] == nums[end] and ans[start+1][end - 1]:
            ans[start][end] = 1

ans_list = []

for _ in range(int(input())):
    s, e = map(int, input().split())
    ans_list.append((ans[s-1][e-1]))

print(*ans_list, sep="\n")