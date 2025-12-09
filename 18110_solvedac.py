import sys


def half_rounding_up(num: float | int) -> int:
    if num >= 0:
        value = int(num + 0.5)
    else:
        value = int(num - 0.5)
    return value


counts = int(sys.stdin.readline())
drop_count = half_rounding_up(counts * 0.15)
difficulties = [0 for _ in range(counts)]
for i in range(counts):
    data = int(sys.stdin.readline())
    difficulties[i] = data
difficulties.sort()
new_difficulties = difficulties[drop_count:counts - drop_count]
if counts == 0:
    result = 0
else:
    result = sum(new_difficulties) / (len(new_difficulties))
print(half_rounding_up(result))
