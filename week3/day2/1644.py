n = int(input())

arr = [False, False] + [True] * (n+1)
primes = []

ans = 0

for i in range(2, n+1):
    if arr[i]:
        primes.append(i)
    for j in range(2*i, n+1, i):
        if arr[j]:
            arr[j] = False

front, back = 0, 0
temp = 0
while True:
    if temp >= n:
        temp -= primes[front]
        front += 1
    elif back == len(primes):
        break
    else:
        temp += primes[back]
        back += 1

    if temp == n:
        ans += 1

print(ans)