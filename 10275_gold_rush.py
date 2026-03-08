import sys


test_count = int(sys.stdin.readline())
for _ in range(test_count):
    n, a, b = map(int, sys.stdin.readline().split())
    i = 0
    while a % 2 == 0:
        a = a >> 1
        i += 1
    print(n - i)
