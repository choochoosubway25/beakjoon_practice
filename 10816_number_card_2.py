import sys

number_size = int(sys.stdin.readline())
number_list = list(map(int, sys.stdin.readline().split()))
target_size = int(sys.stdin.readline())
target_list = list(map(int, sys.stdin.readline().split()))
number_list.sort()
result_list = [0 for _ in range(target_size)]
result = str()
for i in range(target_size):
    target = target_list[i]
    left, right = 0, number_size - 1
    count = 0
    while left < right:
        is_stop = False
        mid_point = left + (right - left) // 2
        if number_list[mid_point] > target:
            right = mid_point
        else:
            left = mid_point


    result += f'{count} '
print(result[:-1])
