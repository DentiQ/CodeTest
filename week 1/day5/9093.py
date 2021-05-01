n = int(input())

for i in range(n):
    arr = input().split()
    ans = []
    for word in arr:
        ans.append(word[::-1])
    print(*ans)
