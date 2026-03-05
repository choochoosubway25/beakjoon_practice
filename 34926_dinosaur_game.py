import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
roads = sys.stdin.readline().strip()
step_set = set()
for _ in range(n):
    if roads[_] == "_":
        step_set.add(_)
next_step = deque()
next_step.append(0)
result = "NO"
visited = set()
while len(next_step) > 0:
    i = next_step.popleft()
    if n - 1 == i:
        result = "YES"
        break
    if i + 1 in step_set and i + 1 not in visited:
        next_step.append(i + 1)
        visited.add(i + 1)
    if i + k in step_set and i + k not in visited:
        next_step.append(i + k)
        visited.add(i + k)
print(result)