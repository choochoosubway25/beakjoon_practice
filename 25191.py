import sys

chicken_count = int(sys.stdin.readline())
cola_count, beer_count = map(int, sys.stdin.readline().split())
maximum_chicken = (cola_count // 2) + beer_count
print(min(maximum_chicken, chicken_count))
