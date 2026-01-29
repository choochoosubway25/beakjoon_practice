import sys

n = int(sys.stdin.readline())
a, b = 0, 1
for i in range(n):
    a, b = b, 2*a+b % 10007
print(b % 10007)
