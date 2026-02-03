import sys

test_count = int(sys.stdin.readline())
sequence = [1, 1, 1]
for _ in range(test_count):
    n = int(sys.stdin.readline())
    if n < len(sequence):
        print(sequence[n-1])
    else:
        a1, a2, a3 = sequence[-3], sequence[-2], sequence[-1]
        for i in range(len(sequence), n):
            a1, a2, a3 = a2, a3, a1+a2
            sequence.append(a3)
        print(sequence[-1])