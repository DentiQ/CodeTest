import sys

input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))

ans = 0

for i in range(n):
    temp = 0
    for j in range(i+1, n):
        if arr[i] > arr[j]:
            temp += 1
        else:
            break
    ans = max(ans, temp)

print(ans)