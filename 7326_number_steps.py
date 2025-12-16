import sys

testing_count = int(sys.stdin.readline())
pos_dict = {(0, 0): 0, (1, 1): 1, (2, 0): 2, (3, 1): 3}
result = str()
for _ in range(testing_count):
    x, y = map(int, sys.stdin.readline().split())
    count = 0
    while y > 1:
        x -= 2
        y -= 2
        count += 1
    try:
        result = pos_dict[(x, y)]
        result = 4 * count + result
        result = str(result)
    except KeyError:
        result = 'No Number'
    print(result)
