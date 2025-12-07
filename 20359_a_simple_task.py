import sys

n = int(sys.stdin.readline())
p = 0
while n % 2 == 0:
    p += 1
    n = n // 2
print(f'{n} {p}')