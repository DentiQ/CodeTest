from sys import stdin

input = stdin.readline

K, N = map(int, input().split())

arr = []

for _ in range(K):
    arr.append(int(input()))

arr.sort()

max_len = arr[-1]
min_len = 1

ans = 0

while min_len <= max_len:
    temp = 0
    my_len = (min_len + max_len) // 2

    for line in arr:
        temp += line // my_len

    if temp < N:
        max_len = my_len - 1
    else:
        ans = my_len
        min_len = my_len + 1

print(ans)
