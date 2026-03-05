import sys

test_count = int(sys.stdin.readline())
for _ in range(test_count):
    case_count = int(sys.stdin.readline())
    sales_list = list(map(int, sys.stdin.readline().split()))
    over_achieved_day = 0
    for j in range(case_count-1):
        for k in range(j+1):
            over_achieved_day += (sales_list[k] <= sales_list[j+1])
    print(over_achieved_day)
