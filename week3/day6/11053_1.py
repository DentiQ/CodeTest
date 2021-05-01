import sys

input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))
max_arr = []

for i in range(n):
    max_arr.append(0)
    for j in range(i):
        if arr[i] > arr[j]:
            max_arr[i] = max(max_arr[i], max_arr[j])
    max_arr[i] += 1

print(max(max_arr))

