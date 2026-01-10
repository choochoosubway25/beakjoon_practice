import sys

price_list = list()
price_list_str = list()
case_count = int(sys.stdin.readline())
for _ in range(case_count):
    price = str(sys.stdin.readline().strip())
    price_list.append(float(price))
    price_list_str.append(price)
least_price = min(price_list)
least_price_index = price_list.index(min(price_list))
price_list.remove(least_price)
second_list_price_index = price_list.index(min(price_list))
if least_price_index <= second_list_price_index:
    second_list_price_index += 1
print(price_list_str[second_list_price_index])
