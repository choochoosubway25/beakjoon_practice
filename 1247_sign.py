import sys

for _ in range(3):
    number_count = int(sys.stdin.readline())
    sums = 0
    for i in range(number_count):
        number = int(sys.stdin.readline())
        sums += number
    if sums > 0:
        print('+')
    elif sums < 0:
        print('-')
    else:
        print('0')
