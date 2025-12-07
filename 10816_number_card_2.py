import sys
from collections import Counter

number_size = int(sys.stdin.readline())
number_list = list(map(int, sys.stdin.readline().split()))
target_size = int(sys.stdin.readline())
target_list = list(map(int, sys.stdin.readline().split()))
result_list = [0 for _ in range(target_size)]
number_count = Counter(number_list)
for i in range(target_size):
    target = target_list[i]
    result_list[i] = number_count[target]
print(*result_list)
