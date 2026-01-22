import sys

while True:
    line = sys.stdin.readline().strip()
    if line == '':
        break
    sequence = list(map(int, line.split()))
    n = sequence[0]
    different = [abs(sequence[i+1] - sequence[i]) for i in range(1, len(sequence)-1)]
    is_jolly = True
    for i in range(1, n):
        if i not in different:
            is_jolly = False
            break
    if is_jolly:
        result = 'Jolly'
    else:
        result = 'Not jolly'
    print(result)
