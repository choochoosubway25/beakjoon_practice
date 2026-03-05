import sys
import math
from bisect import bisect_right

# 기존 입력값을 받음
problem_count, user_count = map(int, sys.stdin.readline().split())
problem_levels = list(map(int, sys.stdin.readline().split()))
user_levels = list(map(int, sys.stdin.readline().split()))
problem_levels.sort()
user_hex_size_list = [0 for _ in range(user_count)]
for i in range(user_count):
    user_level = user_levels[i]
    user_problem_count = bisect_right(problem_levels, user_level)
    if user_problem_count != 0:
        user_hex_size_list[i] = math.floor((3 + math.sqrt(12 * user_problem_count - 3)) / 6)
print(' '.join(map(str, user_hex_size_list)))
