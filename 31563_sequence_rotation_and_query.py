import sys


number_count, query_count = map(int, sys.stdin.readline().split())
sequences = list(map(int, sys.stdin.readline().split()))
sub_sum_sequence = [0 for _ in range(number_count + 1)]
subsum = 0
for i in range(number_count):
    subsum += sequences[i]
    sub_sum_sequence[i + 1] = subsum
zero_pos = 0
for j in range(query_count):
    query_input = sys.stdin.readline().split()
    if query_input[0] == "1":
        shift_length = int(query_input[1])
        zero_pos = (zero_pos - shift_length) % number_count
    elif query_input[0] == "2":
        shift_length = int(query_input[1])
        zero_pos = (zero_pos + shift_length) % number_count
    elif query_input[0] == "3":
        a, b = map(int, query_input[1:])
        start_pos, end_pos = a + zero_pos, b + zero_pos
        if start_pos > number_count:
            start_pos -= number_count
        if end_pos > number_count:
            end_pos -= number_count
        if start_pos <= end_pos:
            print(sub_sum_sequence[end_pos] - sub_sum_sequence[start_pos - 1])
        else:
            print(sub_sum_sequence[-1] - sub_sum_sequence[start_pos - 1] + sub_sum_sequence[end_pos])
