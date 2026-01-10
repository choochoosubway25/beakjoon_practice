import sys

test_count = int(sys.stdin.readline())
for _ in range(test_count):
    number = int(sys.stdin.readline()) + 1
    is_prime = True
    i = 2
    while i ** 2 <= number:
        if number % i == 0:
            is_prime = False
            break
        i += 1
    if is_prime:
        print(1)
        print(f'1 {number}')
    else:
        print(0)
