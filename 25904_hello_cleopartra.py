import sys

player_count, starting_extent = map(int, sys.stdin.readline().split())
maximum_extents = list(map(int, sys.stdin.readline().split()))
current_extents = starting_extent
i = 0
while current_extents <= maximum_extents[i]:
    i = (i + 1) % player_count
    current_extents += 1
print(i + 1)
