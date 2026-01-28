import sys
import heapq

heap = []
heapq.heapify(heap)
operation_count = int(sys.stdin.readline())
for i in range(operation_count):
    num = int(sys.stdin.readline())
    if num > 0:
        heapq.heappush(heap, num)
    else:
        if len(heap) > 0:
            print(heapq.heappop(heap))
        else:
            print(0)
