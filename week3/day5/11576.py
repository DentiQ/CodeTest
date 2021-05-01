a, b = map(int, input().split())
n = int(input())

inputs = list(map(int, input().split()))

sum = 0
for i in range(n):
    sum += inputs[i] * (a**(n-i-1))

ans = list()

while sum != 0:
    ans.append(sum%b)
    sum //= b

print(*ans[::-1])