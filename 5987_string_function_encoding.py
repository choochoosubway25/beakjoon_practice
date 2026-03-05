import sys

test_count = int(sys.stdin.readline())
for _ in range(test_count):
    start_pos, iter_num, strings = sys.stdin.readline().split()
    start_pos = int(start_pos)
    iter_num = int(iter_num)
    new_string = ""
    for i in range(iter_num):
        new_string = strings[start_pos:] + strings
        strings = new_string
    print(strings)
