import sys
import math

n = int(sys.stdin.readline())
square_sum_set = {0}
iter_limit = int(math.sqrt(n)) + 1
result = 0
while n not in square_sum_set:
    result += 1
    new_set = set()
    for i in square_sum_set:
        for j in range(iter_limit):
            new_set.add(i + j ** 2)
    square_sum_set = new_set
print(result)
