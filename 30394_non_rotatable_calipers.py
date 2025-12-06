import sys

n = int(sys.stdin.readline())
y_max = int()
y_min = int()
for i in range(n):
    _, y = map(int, sys.stdin.readline().split())
    if i == 0:
        y_min = y
        y_max = y
    if y < y_min:
        y_min = y
    if y > y_max:
        y_max = y
print(y_max-y_min)
