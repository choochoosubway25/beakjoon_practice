import sys

n, m = map(int, sys.stdin.readline().split())
size_condition = (n != 1) and (m != 1)
s_x, s_y = map(int, sys.stdin.readline().split())
e_x, e_y = map(int, sys.stdin.readline().split())
coordinate_condition = ((s_x + s_y) % 2) == ((e_x + e_y) % 2)
same_position_condition = (s_x == e_x) and (s_y == e_y)
not_same_position_condition = size_condition and coordinate_condition
result = 'NO'
if same_position_condition or not_same_position_condition:
    result = 'YES'
print(result)
