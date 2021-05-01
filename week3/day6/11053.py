import sys

input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))

ans = 0

for i in range(n):
    temp_arr = []
    for num in arr[i:]:
        if not temp_arr or temp_arr[-1] < num:
            temp_arr.append(num)
    print(temp_arr)
    ans = max(ans, len(temp_arr))

print(ans)


