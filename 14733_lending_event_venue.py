import sys
import heapq

rectangle_count = int(sys.stdin.readline())
x_list = list()
y_list = list()
heapq.heapify(x_list)
heapq.heapify(y_list)
rectangle_list = list()
for i in range(rectangle_count):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    rectangle_list.append((x1, y1, x2, y2))
    if x1 not in x_list:
        heapq.heappush(x_list, x1)
    if x2 not in x_list:
        heapq.heappush(x_list, x2)
    if y1 not in y_list:
        heapq.heappush(y_list, y1)
    if y2 not in y_list:
        heapq.heappush(y_list, y2)
x_count = len(x_list)
y_count = len(y_list)
area_dict = dict()
for rect in rectangle_list:
    x1, y1, x2, y2 = rect
    x1_index = x_list.index(x1)
    y1_index = y_list.index(y1)
    x2_index = x_list.index(x2)
    y2_index = y_list.index(y2)
    for i in range(x1_index, x2_index):
        y_dict = dict()
        for j in range(y1_index, y2_index):
            y_dict[y_list[j]] = (x_list[i + 1] - x_list[i]) * (y_list[j + 1] - y_list[j])
        area_dict[x_list[i]] = y_dict
areas = 0
for x in area_dict.keys():
    areas += sum(area_dict[x].values())
print(areas)
