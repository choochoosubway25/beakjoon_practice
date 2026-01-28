import sys

while True:
    line = sys.stdin.readline().strip()
    if line == '0 0':
        break
    x, y = map(int, line.split())
    x_binary = bin(x & 255)
    y_binary = bin(y & 255)
    x_complimentary = bin((~x & 255) + 1)
    y_complimentary = bin((~y & 255) + 1)
    x_minus_y = bin(x - y & 255)
    print(f'{x} = {x_binary[2:]:0>8}')
    print(f'{y} = {y_binary[2:]:0>8}')
    print(f'{-x} = {x_complimentary[2:]:0>8}')
    print(f'{-y} = {y_complimentary[2:]:0>8}')
    print(f'{x - y} = {x_minus_y[2:]:0>8}\n')
