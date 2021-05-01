from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]

for i in range(1, n+1):
    node_list = list(map(int, input().split()))
    for j in range(1, len(node_list)//2):
        graph[node_list[0]].append([node_list[2*j-1], node_list[2*j]])


def bfs(root):
    q = deque()
    q.append((root, 0))
    dis = [-1] * (n + 1)
    dis[root] = 0
    while q:
        v, dist = q.popleft()
        for next_v, next_dist in graph[v]:
            if dis[next_v] == -1:
                dis[next_v] = dist + next_dist
                q.append([next_v, dis[next_v]])
    far = max(dis)
    idx = dis.index(far)
    return far, idx


far_v = bfs(1)[1]
ans = bfs(far_v)[0]

print(ans)