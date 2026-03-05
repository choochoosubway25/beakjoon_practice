import sys

length = int(sys.stdin.readline())
inputs = sys.stdin.readline().strip()
substring_set = set()
for i in range(1, length):
    for j in range(i, length + 1):
        substring_set.add(inputs[j - i:j])
    if len(substring_set) == length - i + 1:
        print(i)
        break
    substring_set.clear()
