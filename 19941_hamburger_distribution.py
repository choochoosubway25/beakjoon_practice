import sys

str_length, distance = map(int, sys.stdin.readline().split())
sequence_str = sys.stdin.readline().strip()
people_index = list()
hamburger_index = set()
for _ in range(str_length):
    if sequence_str[_] == 'P':
        people_index.append(_)
    else:
        hamburger_index.add(_)
result = 0
for i in people_index:
    for j in range(-distance, distance+1):
        if i + j in hamburger_index:
            result += 1
            hamburger_index.remove(i + j)
            break
print(result)
