import sys

n, k = map(int, sys.stdin.readline().split())
a = [list() for _ in range(n)]
for _ in range(n):
    rows = list(map(int, sys.stdin.readline().split()))
    a[_] = rows
k, m = map(int, sys.stdin.readline().split())
b_t = [[0 for _ in range(k)] for _ in range(m)]
for i in range(k):
    columns = list(map(int, sys.stdin.readline().split()))
    for j in range(m):
        b_t[j][i] = columns[j]
result = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        result[i][j] = sum([c * d for c, d in zip(a[i], b_t[j])])
for rows in result:
    print(*rows)
