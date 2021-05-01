n, k = map(int, input().split())

arr = [1] * (n+1)

for i in range(2, n+1):
    for j in range(i, n+1, i):
        if arr[j] == 1:
            arr[j] = 0
            k -= 1
            if k == 0:
                print(j)
                break