import sys

bomb_rows = set()
bomb_columns = set()
start_x, start_y = map(int, sys.stdin.readline().split())
for i in range(10):
    board_row = sys.stdin.readline().strip()
    for j in range(10):
        if board_row[j] == "o":
            bomb_rows.add(i+1)
            bomb_columns.add(j+1)
row_min, column_min = 100, 100
safe_row = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10} - bomb_rows
safe_column = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10} - bomb_columns
for row in safe_row:
    row_min = min(row_min, abs(row - start_x))
for column in safe_column:
    column_min = min(column_min, abs(column - start_y))
print(row_min + column_min)
