import sys
from collections import Counter

row_count, column_count = map(int, input().split())
result = 0
row_counter = Counter()
for _ in range(row_count):
    inputs = sys.stdin.readline().split()
    row_counter.update(inputs)
print(row_counter.most_common(1)[0][1])
