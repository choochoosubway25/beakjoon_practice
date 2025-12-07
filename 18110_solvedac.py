import sys

counts = int(sys.stdin.readline())
drop_count = round(counts * 0.15)
difficulties = [0 for _ in range(counts)]
for i in range(counts):
    data = int(sys.stdin.readline())
    difficulties[i] = data
difficulties.sort()
new_difficulties = difficulties[drop_count:counts - drop_count]
if counts == 0:
    result = 0
else:
    result = sum(new_difficulties) / (counts - (2 * drop_count))
print(round(result))
