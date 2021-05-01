n, m = map(int, input().split())

q = [i for i in range(1, n+1)]

nums = list(map(int, input().split()))

ans = 0

for num in nums:
    idx = q.index(num)

    if idx > len(q) - idx:
        while True:
            if q[0] == num:
                q.pop(0)
                break
            else:
                q.insert(0, q.pop())
                ans += 1
    else:
        while True:
            if q[0] == num:
                q.pop(0)
                break
            else:
                q.append(q.pop(0))
                ans += 1

print(ans)
