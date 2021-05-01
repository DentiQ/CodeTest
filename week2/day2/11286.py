import heapq
import sys
heap = []

N = int(sys.stdin.readline())

for i in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        try:
            print(heapq.heappop(heap)[1])
        except:
            print(0)
    else:
        heapq.heappush(heap, (abs(x), x))




