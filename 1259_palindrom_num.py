while True:
    number = int(input())
    if number == 0:
        break
    num_str = str(number)
    result = 'yes'
    for i in range(0, len(num_str)//2):
        if num_str[i] != num_str[-i-1]:
            result = 'no'
    print(result)