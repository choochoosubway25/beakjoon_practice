import sys


length = int(sys.stdin.readline())
repeat_num = (length + 1) // 3
if (length + 1) % 3 != 0:
    repeat_num += 1
basic_string = "HSS" * repeat_num
print(basic_string[1:length+1])
