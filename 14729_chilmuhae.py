import sys
import heapq

n = int(sys.stdin.readline())
scores = list()
heapq.heapify(scores)
for _ in range(n):
    heapq.heappush(scores, float(sys.stdin.readline()))
for i in range(7):
    result = heapq.heappop(scores)
    integer, decimal = str(result).split('.')
    print(f"{integer}.{decimal:<03}")
