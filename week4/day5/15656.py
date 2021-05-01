import sys
from itertools import combinations_with_replacement

input = sys.stdin.readline

n, m = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()

for nums in list(combinations_with_replacement(arr, m)):
    print(*nums)
