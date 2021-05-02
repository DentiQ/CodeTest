from sys import stdin

input = stdin.readline

N = int(input())

chemical = list(map(int, input().split()))

chemical.sort()

front, rear = 0, N-1

ans = chemical[front] + chemical[rear]
af, ar = front, rear

while True:
    temp = chemical[front] + chemical[rear]
    if abs(ans) > abs(temp):
        af, ar = front, rear
        ans = temp
        if temp == 0:
            print(chemical[af], chemical[ar])
            break
    if temp < 0:
        front += 1
    else:
        rear -= 1
    if front >= rear:
        print(chemical[af], chemical[ar])
        break
