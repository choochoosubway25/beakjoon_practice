import sys

test_count = int(sys.stdin.readline())
for _ in range(test_count):
    candy_type_num, candy_least_sufficient = map(int, sys.stdin.readline().split())
    candy_stock_num = list(map(int, sys.stdin.readline().split()))
    result = sum(map(lambda x: x // candy_least_sufficient, candy_stock_num))
    print(result)
