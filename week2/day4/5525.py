n = int(input())
p = int(input())
s = input()

counter = 0
arr = []
i = 0
while i < p-2:
    if s[i] == 'I' and s[i+1] == 'O' and s[i+2] == 'I':
        counter += 1
        i += 2
    else:
        arr.append(counter)
        counter = 0
        i += 1

if counter != 0:
    arr.append(counter)

ans = 0

for i in arr:
    if i >= n:
        ans += i-n+1

print(ans)



