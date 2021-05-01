n = int(input())

arr = list(map(int, input().split()))
stack = [0]
ans = [-1 for i in range(n)]

for i in range(1, n):
    while stack and arr[stack[-1]] < arr[i]:
        ans[stack[-1]] = arr[i]
        stack.pop()
    stack.append(i)

print(*ans)