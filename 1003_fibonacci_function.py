import sys

fibonacci_list = [0, 1]
test_count = int(sys.stdin.readline())
for _ in range(test_count):
    cases = int(sys.stdin.readline())
    if cases == 0:
        print('1 0')
        continue
    noted_index_until = len(fibonacci_list)
    if cases >= noted_index_until:
        for i in range(noted_index_until, cases + 1):
            next_term = fibonacci_list[i - 2] + fibonacci_list[i - 1]
            fibonacci_list.append(next_term)
    print(f'{fibonacci_list[cases - 1]} {fibonacci_list[cases]}')
