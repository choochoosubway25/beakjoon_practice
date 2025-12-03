import sys

number_size = int(sys.stdin.readline())
number_list = list(map(int, sys.stdin.readline().split()))
target_size = int(sys.stdin.readline())
target_list = list(map(int, sys.stdin.readline().split()))
number_list.sort()
for j in range(target_size):
    target = target_list[j]
    left = 0
    right = number_size-1
    is_found = False
    while left <= right:
        mid_point = left + (right-left) // 2
        if target > number_list[mid_point]:
            left = mid_point+1
        elif target < number_list[mid_point]:
            right = mid_point-1
        else:
            is_found = True
            break
    if is_found:
        print(1)
    else:
        print(0)
