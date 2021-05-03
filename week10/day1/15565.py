from sys import stdin

input = stdin.readline

N, K = map(int, input().split())
dolls = list(map(int, input().split()))

front = 0
end = front + K
cnt = 0

ans = float("inf")

for doll in dolls[front:end+1]:
    if doll == 1:
        cnt += 1

while True:
    if cnt < K:
        end += 1
        if end < N:
            if dolls[end] == 1:
                cnt += 1
        else:
            break
    elif cnt >= K:
        ans = min(ans, end - front + 1)
        if dolls[front] == 1:
            cnt -= 1
        front += 1

if cnt == K:
    ans = min(ans, end - front + 1)

if ans != float("inf"):
    print(ans)
else:
    print(-1)