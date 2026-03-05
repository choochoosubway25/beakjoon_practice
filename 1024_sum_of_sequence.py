import sys

target_sum, minimum_length = map(int, sys.stdin.readline().split())
length = minimum_length
sequences = [-1]
while length <= 100:
    means = target_sum // length
    if means + 1 < (length // 2):
        break
    if length % 2 == 0:
        if target_sum % length != 0 and 2 * target_sum % length == 0:
            sequences = list()
            start = -(length // 2) + 1
            end = (length // 2) + 1
            for i in range(start, end):
                sequences.append(means + i)
            break
    else:
        if target_sum % length == 0:
            sequences = list()
            start = -(length // 2)
            end = (length // 2) + 1
            for i in range(start, end):
                sequences.append(means + i)
            break
    length += 1
print(' '.join(map(str, sequences)))
