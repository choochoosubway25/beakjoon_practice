import sys
from queue import Queue

n, k = map(int, sys.stdin.readline().split())
humans = Queue()
result = '<'
for _ in range(n):
    humans.put(_+1)
for i in range(n):
    for _ in range(k-1):
        human = humans.get()
        humans.put(human)
    else:
        human_out = humans.get()
    result += f'{human_out}, '
result = result[:-2] + '>'
print(result)
