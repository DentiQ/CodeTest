from sys import stdin

input = stdin.readline

N = int(input())

now = list(map(int, input().strip()))
goal = list(map(int, input().strip()))

now2 = [abs(1 - now[0])] + [abs(1 - now[1])] + now[2:]

count1, count2 = 0, 1
flag1, flag2 = False, False

for i in range(1, N):
    if now[i - 1] != goal[i - 1]:
        count1 += 1
        now[i - 1] = abs(1-now[i-1])
        now[i] = abs(1-now[i])
        if i != N-1:
            now[i+1] = abs(1-now[i+1])

if now == goal:
    flag1 = True

for i in range(1, N):
    if now2[i - 1] != goal[i - 1]:
        count2 += 1
        now2[i - 1] = abs(1 - now2[i - 1])
        now2[i] = abs(1 - now2[i])
        if i != N - 1:
            now2[i + 1] = abs(1 - now2[i + 1])

if now2 == goal:
    flag2 = True

if flag1 and flag2:
    print(min(count1, count2))
elif flag1:
    print(count1)
elif flag2:
    print(count2)
else:
    print(-1)
