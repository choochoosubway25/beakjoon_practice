import sys

n = int(sys.stdin.readline())
sequences = list()
for _ in range(n):
    number = int(sys.stdin.readline())
    sequences.append(number)
stack = list()
result_list = list()
is_sequence_able = True
i = 1
for num in sequences:
    while i <= num:
        stack.append(i)
        i += 1
        result_list.append('+')
    if stack[-1] != num:
        is_sequence_able = False
        break
    else:
        stack.pop()
        result_list.append('-')
if is_sequence_able:
    for operation in result_list:
        print(operation)
else:
    print('NO')
