import heapq
import sys
heap = []

while True:
    x = int(sys.stdin.readline())
    if x == 0:
        try:
            heapq.heappop(heap)
            print(heap)
        except:
            print(0)
    else:
        heapq.heappush(heap, (abs(x), x))