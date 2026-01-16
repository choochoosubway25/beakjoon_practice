import sys

case_count = int(sys.stdin.readline())
least_price = 0
second_least_price = 0
for i in range(case_count):
    price_str = str(sys.stdin.readline().strip())
    price = float(price_str)
    if i == 0:
        least_price = price
    else:
        if price < least_price:
            least_price, second_least_price = price, least_price
        elif i == 1 or price < second_least_price:
            second_least_price = price
print(f'{second_least_price:.2f}')
