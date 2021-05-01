import sys
import heapq

input = sys.stdin.readline

n = int(input())

arr = []

ans = 0

for i in range(n):
    heapq.heappush(arr, int(input()))

while len(arr) > 1:
    a = heapq.heappop(arr)
    b = heapq.heappop(arr)
    heapq.heappush(arr, a+b)
    ans += a+b

print(ans)

