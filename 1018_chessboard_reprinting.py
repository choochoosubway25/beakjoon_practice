import sys


def rows_to_binary(row: str) -> str:
    result = '0b'
    for chars in row:
        if chars == 'W':
            result += '0'
        elif chars == 'B':
            result += '1'
        else:
            pass
    return result


rows, columns = map(int, sys.stdin.readline().split())
board = list()
standard = int('0b10101010', 2)
min_result = -1
for _ in range(rows):
    row = str(sys.stdin.readline())
    board.append(row)
for i in range(rows - 7):
    for j in range(columns - 7):
        sub_board = board[i:i+8]
        correction_count = 0
        for k in range(8):
            sub_row = sub_board[k][j:j+8]
            binary_row = int(rows_to_binary(sub_row), 2)
            if k % 2 == 0:
                correction_count += bin(binary_row ^ standard).count('1')
            else:
                correction_count += bin(binary_row ^ (~standard & 255)).count('1')
        results = min(correction_count, 64 - correction_count)
        if results < min_result or min_result < 0:
            min_result = results
print(min_result)
