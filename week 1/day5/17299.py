n = int(input())

arr = list(map(int, input().split()))
stack = []
ans = [-1 for i in range(n)]

counter = dict()

for i in arr:
    try:
        counter[i] += 1
    except:
        counter[i] = 1

stack.append(0)

for i in range(1, n):
    while stack and counter[arr[stack[-1]]] < counter[arr[i]]:
        ans[stack[-1]] = arr[i]
        stack.pop()
    stack.append(i)

print(*ans)