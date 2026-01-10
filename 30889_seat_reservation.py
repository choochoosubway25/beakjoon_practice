import sys

seat_map = [['.'] * 20 for _ in range(10)]
ticket_count = int(sys.stdin.readline())
for i in range(ticket_count):
    seat_num = str(sys.stdin.readline().strip())
    row_num = ord(seat_num[0]) - 65
    column_num = int(seat_num[1:]) - 1
    seat_map[row_num][column_num] = 'o'
for i in range(10):
    result = ''.join(seat_map[i][:])
    print(result)
