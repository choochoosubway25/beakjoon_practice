import sys

height, width = map(int, sys.stdin.readline().split())
flags = []
for _ in range(height):
    rows = sys.stdin.readline().strip()
    flags.append(rows)
fixed_value = (width - flags[0].count("W")) + (width - flags[-1].count("R"))
white_list = []
blue_list = []
red_list = []
result = None
for i1 in range(1, height - 1):
    blue_list.append(width - flags[i1].count("B"))
    if i1 != height - 2:
        white_list.append(width - flags[i1].count("W"))
    if i1 != 1:
        red_list.append(width - flags[i1].count("R"))
for i in range(height-2):
    for j in range(1+i, height-1):
        counts = sum(white_list[:i]) + sum(blue_list[i:j]) + sum(red_list[j-1:])
        if result is None:
            result = counts
        else:
            result = min(result, counts)
print(result + fixed_value)
