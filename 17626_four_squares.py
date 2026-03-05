import sys
import math

n = int(sys.stdin.readline())
square_sum_set = {n}
iter_limit = int(math.sqrt(n)) + 1
squared_numbers = set([ii ** 2 for ii in range(1, iter_limit)])
result = 0
is_square = False
for _ in range(4):
    result += 1
    new_set = set()
    for num in square_sum_set:
        if num in squared_numbers:
            is_square = True
            break
        iter_limit = int(math.sqrt(num)) + 1
        for j in range(iter_limit // 2, iter_limit):
            new_num = num - j ** 2
            if new_num > 0:
                new_set.add(new_num)
    if is_square:
        break
    square_sum_set = new_set
print(result)
