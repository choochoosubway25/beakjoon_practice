import sys
from collections import Counter

hour_count = int(sys.stdin.readline())
group_list = list()
group_counter = Counter()
for _ in range(hour_count):
    inputs = sys.stdin.readline().split()
    element = set(inputs)
    if element not in group_list:
        group_list.append(element)
    group_index = group_list.index(element)
    group_counter[group_index] += 1
most_freq = group_counter.most_common(1)[0][1]
print(most_freq)
