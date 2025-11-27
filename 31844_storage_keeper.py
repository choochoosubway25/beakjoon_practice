import sys

status_str = str(sys.stdin.readline().strip())
robot_pos = -1
box_pos = -1
goal_pos = -1

for i in range(len(status_str)):
    if status_str[i] == '@':
        robot_pos = i
    if status_str[i] == '#':
        box_pos = i
    if status_str[i] == '!':
        goal_pos = i

result = 0
# 목표에 도달 불가능한 시나리오
# 1. 로봇 기준, 박스와 목표가 서로 다른 방향에 있음
is_different = (robot_pos - box_pos) * (robot_pos - goal_pos) < 0
# 2. 로봇 기준, 박스가 목표보다 거리가 더 멈
is_faraway = abs(robot_pos - goal_pos) < abs(robot_pos - box_pos)
is_not_reachable = is_faraway or is_different
if is_not_reachable:
    result = -1
else:
    result = abs(robot_pos - goal_pos) - 1
print(result)
