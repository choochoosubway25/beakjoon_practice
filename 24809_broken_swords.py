import sys

sword_count = int(sys.stdin.readline())
top_count = 0
right_count = 0
for _ in range(sword_count):
    position_string = str(sys.stdin.readline().strip())
    top_string = position_string[:2]
    right_string = position_string[2:]
    top_count += top_string.count('0')
    right_count += right_string.count('0')
renew_count = min(top_count // 2, right_count // 2)
top_remained = top_count - (2 * renew_count)
right_remained = right_count - (2 * renew_count)
print(f'{renew_count} {top_remained} {right_remained}')
