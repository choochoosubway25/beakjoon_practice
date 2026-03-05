import sys


test_count = int(sys.stdin.readline())
for _ in range(test_count):
    n = int(sys.stdin.readline())
    count_five = 0
    five_time = 5
    while n // five_time > 0:
        count_five += n // five_time
        five_time = five_time * 5
    print(count_five)
