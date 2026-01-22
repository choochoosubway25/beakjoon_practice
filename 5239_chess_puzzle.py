import sys

test_count = int(sys.stdin.readline())
for _ in range(test_count):
    inputs = list(map(int, sys.stdin.readline().split()))
    rook_count = inputs[0]
    column_list = [0 for _ in range(rook_count)]
    row_list = [0 for _ in range(rook_count)]
    result = 'SAFE'
    for i in range(rook_count):
        column, row = inputs[2*i+1], inputs[2*i+2]
        if column in column_list or row in row_list:
            result = 'NOT ' + result
            break
        column_list[i] = column
        row_list[i] = row
    print(result)
