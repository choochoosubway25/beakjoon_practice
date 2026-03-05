import sys

rectangle_count = int(sys.stdin.readline())
total_rectangle = [[0 for i in range(500)] for j in range(500)]
for _ in range(rectangle_count):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            total_rectangle[i][j] = 1
print(sum(sum(row) for row in total_rectangle))
