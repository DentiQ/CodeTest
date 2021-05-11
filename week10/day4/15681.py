import sys

sys.setrecursionlimit(100000000)

input = sys.stdin.readline

N, R, Q = map(int, input().split())

tree = [[] for _ in range(N+1)]
cnt = [0] * (N+1)

for _ in range(N-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)


def cnt_node(i):
    cnt[i] = 1
    for node in tree[i]:
        if cnt[node] == 0:
            cnt_node(node)
            cnt[i] += cnt[node]
    return


cnt_node(R)

for _ in range(Q):
    q = int(input())
    print(cnt[q])
