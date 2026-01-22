import sys

while True:
    input_str = sys.stdin.readline().strip()
    if input_str == '':
        break
    inputs = input_str.split()
    basket_num = int(inputs[0])
    coin_weight = int(inputs[1])
    lighter_weight = int(inputs[2])
    total_weight = int(inputs[3])
    estimated_weight = (basket_num - 1) * basket_num * coin_weight // 2
    difference = estimated_weight - total_weight
    result = difference // lighter_weight
    if result == 0:
        result = basket_num
    print(result)
