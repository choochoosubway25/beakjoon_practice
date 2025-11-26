import heapq
import sys

iter_num = int(sys.stdin.readline())
data_heap = []

for i in range(iter_num):
    age, name = map(str, sys.stdin.readline().split())
    data = (int(age), i, name)
    heapq.heappush(data_heap, data)

for _ in range(iter_num):
    sorted_data = heapq.heappop(data_heap)
    print(f'{sorted_data[0]} {sorted_data[2]}')
