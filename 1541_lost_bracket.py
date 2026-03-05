import sys


operations = sys.stdin.readline()
sub_operation = operations.split('-')
total = sum(map(int, sub_operation[0].split('+')))
for i in range(1, len(sub_operation)):
    total -= sum(map(int, sub_operation[i].split('+')))
print(total)
