import sys

test_count = int(sys.stdin.readline())
prize_first = \
    {1: 5000000, 2: 3000000, 3: 2000000,
     4: 500000, 5: 300000, 6: 100000}
prize_second = \
    {1: 5120000, 2: 2560000, 3: 1280000, 4: 640000, 5: 320000}
winner_count_first = [1, 2, 3, 4, 5, 6]
winner_count_second = [1, 2, 4, 8, 16]
for _ in range(test_count):
    result = 0
    first, second = map(int, sys.stdin.readline().split())
    if first > 0:
        i = 1
        total = 0
        for j in winner_count_first:
            total += j
            if first <= total:
                break
            i += 1
        try:
            result += prize_first[i]
        except KeyError:
            pass
    if second > 0:
        i = 1
        total = 0
        for k in winner_count_second:
            total += k
            if second <= total:
                break
            i += 1
        try:
            result += prize_second[i]
        except KeyError:
            pass
    print(result)
