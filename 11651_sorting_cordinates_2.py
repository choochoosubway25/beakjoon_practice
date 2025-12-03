import sys
import heapq

num_iter = int(sys.stdin.readline())
cordinate_heap = list()
for _ in range(num_iter):
    x, y = map(int, sys.stdin.readline().split())
    heapq.heappush(cordinate_heap, (y, x))
for _ in range(num_iter):
    data = heapq.heappop(cordinate_heap)
    print(f"{data[1]} {data[0]}")
