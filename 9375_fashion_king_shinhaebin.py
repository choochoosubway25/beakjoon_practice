import sys

test_count = int(sys.stdin.readline())
for _ in range(test_count):
    clothes_dict = dict()
    clothes_count = int(sys.stdin.readline())
    for k in range(clothes_count):
        cloth, kind = map(str, sys.stdin.readline().split())
        if kind not in clothes_dict.keys():
            clothes_dict[kind] = [cloth]
        else:
            clothes_dict[kind].append(cloth)
    result = 1
    for value in clothes_dict.values():
        result *= (len(value) + 1)
    print(result - 1)
