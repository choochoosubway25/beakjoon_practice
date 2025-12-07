import sys

t = int(sys.stdin.readline())
for i in range(t):
    result = 0
    n = int(sys.stdin.readline())
    if n % 2 == 0:
        result = 2 ** (n // 2)
    print(result)
