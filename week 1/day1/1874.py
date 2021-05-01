#1874번
stack = []
goal = []

ans = []

index = 0
goal_index = 0

n = int(input())

for i in range(n):
    goal.append(int(input()))

for i in range(1, n+1):
    stack.append(i)
    ans.append('+')
    while( stack and stack[-1] == goal[goal_index]):
        stack.pop()
        ans.append('-')
        goal_index = goal_index + 1

if stack:
    print("NO")
else:
    for i in ans:
        print(i)