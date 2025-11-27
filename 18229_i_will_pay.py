import sys

human_num, repeat_num, distance = map(int, sys.stdin.readline().split())
matrix = list()
for _ in range(human_num):
    distance_list = list(map(int, sys.stdin.readline().split()))
    matrix.append(distance_list)
total_list = [0 for _ in range(human_num)]
finish_condition = False
for j in range(repeat_num):
    for i in range(human_num):
        total_list[i] += matrix[i][j]
        if total_list[i] >= distance:
            finish_condition = True
            break
    if finish_condition:
        break
print(f'{i+1} {j+1}')
