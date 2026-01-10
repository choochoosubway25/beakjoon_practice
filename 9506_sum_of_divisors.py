import sys

while True:
    number = int(sys.stdin.readline())
    if number < 0:
        break
    i = 2
    divisor_list = [1]
    while i * i < number:
        if number % i == 0:
            divisor_list.append(i)
            divisor_list.append(number // i)
        i += 1
    divisor_list.sort()
    is_perfect = sum(divisor_list) == number
    if is_perfect:
        result = f'{number} ='
        for divisor in divisor_list:
            result += f' {divisor} +'
        print(result[:-2])
    else:
        print(f'{number} is NOT perfect.')
