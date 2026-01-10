import sys

day_count = int(sys.stdin.readline())
price_list = list(map(int, sys.stdin.readline().split()))
max_earn = 0
lowest_day = 0
for i in range(1, day_count):
    earn_today = price_list[i] - price_list[lowest_day]
    if earn_today > max_earn:
        max_earn = earn_today
    if price_list[i] < price_list[lowest_day]:
        lowest_day = i
print(max_earn)
