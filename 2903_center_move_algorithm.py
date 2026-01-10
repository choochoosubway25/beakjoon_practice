import sys

n = int(sys.stdin.readline())
for i in range(n+1):
    row_dots = 1 + 2 ** i
total_dots = row_dots ** 2
print(total_dots)
