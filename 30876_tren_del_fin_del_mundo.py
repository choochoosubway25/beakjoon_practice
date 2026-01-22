import sys

station_count = int(sys.stdin.readline())
minimum_y = 0
minimum_x = 0
for i in range(station_count):
    x, y = map(int, sys.stdin.readline().split())
    if i == 0:
        minimum_x, minimum_y = x, y
    else:
        if y < minimum_y:
            minimum_x, minimum_y = x, y
print(minimum_x, minimum_y)
