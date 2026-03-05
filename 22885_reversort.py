import sys


test_count = int(sys.stdin.readline())

for _ in range(test_count):
    result = 0
    list_length = int(sys.stdin.readline())
    sorting_list = list(map(int, sys.stdin.readline().split()))
    for i in range(list_length - 1):
        sub_list = sorting_list[i:list_length]
        minimum = min(sub_list)
        j = sub_list.index(minimum) + i
        result += j - i + 1
        sorting_list[i:j+1] = sorting_list[i:j+1][::-1]
    print(f"Case #{_+1}: {result}")