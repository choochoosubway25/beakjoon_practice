import sys


rows, columns = map(int, sys.stdin.readline().split())
strings = []
for _ in range(rows):
    strings.append(sys.stdin.readline().strip())
degrees = int(sys.stdin.readline())
# 180도 이상이면 내용을 뒤집어서 계산한다.
degrees = degrees % 360
if 180 <= degrees:
    for i1 in range(rows):
        strings[i1] = strings[i1][::-1]
    strings = strings[::-1]
    degrees = degrees % 180
if degrees == 45: # 45도의 경우
    new_strings = []
    for j in range(rows + columns - 1):
        new_row = []
        for k in range(min(j, rows-1), -1, -1):
            if j - k < columns:
                new_row.append(strings[k][j-k])
            else:
                new_strings.append(" ".join(new_row))
                break
        else:
            new_strings.append(" ".join(new_row))
    # 적당한 공백을 삽입한다.
    for l1 in range(rows):
        new_strings[l1] = " " * (rows - 1 - l1) + new_strings[l1]
    for l2 in range(columns):
        new_strings[rows + l2 - 1] = " " * l2 + new_strings[rows + l2 - 1]
elif degrees == 90:
    new_strings = []
    for j in range(columns):
        new_row = []
        for k in range(rows):
            new_row.append(strings[k][j])
        new_row = new_row[::-1]
        new_strings.append("".join(new_row))
elif degrees == 135: # 135도의 경우
    new_strings = []
    for j in range(rows + columns - 1):
        new_row = []
        for k in range(min(j + 1, rows)):
            if j - k < columns:
                new_row.append(strings[rows - 1 - k][j - k])
        else:
            new_strings.append(" ".join(new_row))
    # 적당한 공백을 삽입한다.
    for l1 in range(rows):
        new_strings[columns + l1 - 1] = " " * l1 + new_strings[columns + l1 - 1]
    for l2 in range(columns):
        new_strings[l2] = " " * (columns - 1 - l2) + new_strings[l2]
else:
    new_strings = strings
for row in new_strings:
    print(row)