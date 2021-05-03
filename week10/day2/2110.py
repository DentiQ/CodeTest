from sys import stdin

N, C = map(int, input().split())

arr = []

for _ in range(N):
    arr.append(int(input()))

arr.sort()

min_gap = arr[1] - arr[0]
max_gap = arr[-1] - arr[0]
ans = 0

while min_gap <= max_gap:
    gap = (min_gap + max_gap) // 2
    current = arr[0]
    cnt = 1
    for i in range(1, N):
        if arr[i] >= current + gap:
            current = arr[i]
            cnt += 1

    if cnt >= C:
        min_gap = gap + 1
        ans = gap
    else:
        max_gap = gap - 1

print(ans)