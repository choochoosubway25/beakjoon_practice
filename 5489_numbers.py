import sys
from collections import Counter

number_count = int(sys.stdin.readline())
number_dict = Counter()
for _ in range(number_count):
    number = int(sys.stdin.readline())
    number_dict.update([number])
most_common_times = number_dict.most_common(1)[0][1]
commons = list()
for key in number_dict.keys():
    if number_dict[key] == most_common_times:
        commons.append(key)
print(min(commons))
