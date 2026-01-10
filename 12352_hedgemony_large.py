import sys

test_count = int(sys.stdin.readline())
for i in range(test_count):
    bushes_count = int(sys.stdin.readline())
    bushes_positions = list(map(float, sys.stdin.readline().split()))
    for j in range(1, bushes_count - 1):
        side_avg = (bushes_positions[j - 1] + bushes_positions[j + 1]) / 2
        if side_avg < bushes_positions[j]:
            bushes_positions[j] = side_avg
    result = bushes_positions[bushes_count - 2]
    print(f'Case #{i + 1}: {result:0.6f}')
