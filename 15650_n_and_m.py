import sys
import queue

n, m = map(int, sys.stdin.readline().split())
data_queue = queue.Queue()
for i in range(1, m+1):
    if i == 1:
        for j in range(1, n+1):
            data_queue.put(f'{j}')
    else:
        for _ in range(data_queue.qsize()):
            data = data_queue.get()
            starting = int(data[-1])
            for j in range(starting+1, n+1):
                data_queue.put(f'{data} {j}')
while data_queue.qsize() > 0:
    data = data_queue.get()
    print(data)
