import sys

test_count = int(sys.stdin.readline())
for i in range(test_count):
    a, b = map(int, sys.stdin.readline().split())
    print(f"Case {i+1}: {a+b}")