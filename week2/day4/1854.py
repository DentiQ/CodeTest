import sys
import heapq

n, m, k = map(int, input().split())
D = [[] for _ in range(n+1)]
S = [[] for _ in range(n+1)]

for _ in range(m):
    i, j, dist = map(int, sys.stdin.readline().split())
    D[i].append((j, dist))

q = []
heapq.heappush(q, (0, 1))
S[1] = [0]

while q:
    t, x = heapq.heappop(q)
    for nx, nt in D[x]:
        if len(S[nx]) < k:
            S[nx] = sorted(S[nx] + [nt + t])
            heapq.heappush(q, [nt + t, nx])
        elif len(S[nx]) == k and S[nx][k - 1] > nt + t:
            S[nx][k - 1] = nt + t
            S[nx].sort()
            heapq.heappush(q, [nt + t, nx])

for i in range(1,n+1):
    print(-1 if len(S[i])<k else S[i][k-1])

