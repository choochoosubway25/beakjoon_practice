import sys

dwarves = list()
for _ in range(9):
    dwarf = int(sys.stdin.readline())
    dwarves.append(dwarf)
target_num = sum(dwarves) - 100
fakes = list()
for i in range(9):
    is_found = False
    for j in range(i+1, 9):
        if dwarves[i] + dwarves[j] == target_num:
            fakes.append(i)
            fakes.append(j)
            is_found = True
            break
    if is_found:
        break
for k in range(9):
    if k not in fakes:
        print(dwarves[k])
