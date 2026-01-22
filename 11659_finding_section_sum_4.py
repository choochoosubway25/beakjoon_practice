import sys

number_count, test_count = map(int, sys.stdin.readline().split())
number_sum_list = [0 for _ in range(number_count + 1)]
number_inputs = map(int, sys.stdin.readline().split())
n = 1
before_number = 0
for number in number_inputs:
    new_number = before_number + number
    number_sum_list[n] = new_number
    before_number = new_number
    n += 1
for k in range(test_count):
    i, j = map(int, sys.stdin.readline().split())
    print(number_sum_list[j] - number_sum_list[i-1])
