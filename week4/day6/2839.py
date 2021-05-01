n = int(input())

ans = [0, 0, 0, 1, -1, 1, 2, -1, 2]

if n % 5 == 0:
        ans = n // 5
        print(ans)
else:
    ans = 0
    while True:
        n -= 3
        ans += 1
        if n % 5 == 0:
            ans += n // 5
            print(ans)
            break
        if n < 0:
            print(-1)
            break





