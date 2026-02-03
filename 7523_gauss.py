import sys

test_count = int(sys.stdin.readline())
for _ in range(test_count):
    start, end = map(int, sys.stdin.readline().split())
    result = end * (end + 1) // 2 - start * (start - 1) // 2
    print(f'Scenario #{_+1}:')
    print(result)
    print()
