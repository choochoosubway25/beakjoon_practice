import sys

n, m = map(int, sys.stdin.readline().split())
not_heard = set()
not_seem = set()
for _ in range(n):
    name = str(sys.stdin.readline().strip())
    not_heard.add(name)
for _ in range(m):
    name = str(sys.stdin.readline().strip())
    not_seem.add(name)
result_set = not_heard & not_seem
result_list = list(result_set)
result_list.sort()
print(len(result_list))
for name in result_list:
    print(name)
