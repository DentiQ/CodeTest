from sys import stdin

input = stdin.readline

N, M = map(int, input().split())

num_arr = [0] + list(map(int, input().split()))

for i in range(1, N+1):
    num_arr[i] += num_arr[i-1]

for _ in range(M):
    s, e = map(int, input().split())
    print(num_arr[e] - num_arr[s-1])