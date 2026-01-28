import sys


while True:
    line = sys.stdin.readline().strip()
    if line == '0':
        break
    number_count = int(line)
    time_list = list()
    is_conflict = False
    for i in range(number_count):
        start, end = sys.stdin.readline().split('-')
        start_time = int(start[0:2]) * 60 + int(start[3:5])
        end_time = int(end[0:2]) * 60 + int(end[3:5])
        time_list.append((start_time, end_time))
    for i in range(number_count):
        first_time, second_time = time_list[i]
        for j in range(i, number_count):
            if time_list[j][0] < first_time < time_list[j][1]:
                is_conflict = True
                break
            if time_list[j][0] < second_time < time_list[j][1]:
                is_conflict = True
                break
    if is_conflict:
        print('conflict')
    else:
        print('no conflict')
