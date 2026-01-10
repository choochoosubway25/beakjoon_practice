import sys


def find_gcd(a, b):
    if b > a:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a


tree_count = int(sys.stdin.readline())
tree_positions = [0 for _ in range(tree_count)]
minimum_distance = 0
for i in range(tree_count):
    tree_positions[i] = int(sys.stdin.readline())
distances = [tree_positions[j + 1] - tree_positions[j] for j in range(tree_count - 1)]
for k in range(tree_count - 1):
    minimum_distance = find_gcd(minimum_distance, distances[k])
result = sum(map(lambda x: (x // minimum_distance) - 1, distances))
print(result)
