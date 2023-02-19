x = int(input())

floor = 0
i = 0
d = 1
while i < x:
    i += d
    d += 1
    floor += 1
if floor % 2 == 0:
    print('{}/{}'.format(floor-(i-x), i-x+1))
else:
    print('{}/{}'.format(i-x+1, floor-(i-x)))