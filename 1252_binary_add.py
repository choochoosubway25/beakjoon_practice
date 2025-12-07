import sys

a, b = map(str, sys.stdin.readline().split())
a = int(a, 2)
b = int(b, 2)
add = bin(a + b)
result = add[2:]
print(result)
