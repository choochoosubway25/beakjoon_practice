import sys

while True:
    number = int(sys.stdin.readline())
    if number == 0:
        break
    sums = 0
    i = 1
    while i <= number:
        sums += i ** 2
        i += 1
    print(sums)
