import sys

character_count = int(sys.stdin.readline())
character_levels = [0 for _ in range(character_count)]
union_criteria = [60, 100, 140, 200, 250]
for i in range(character_count):
    level = int(sys.stdin.readline())
    character_levels[i] = level
character_levels.sort(reverse=True)
union_count = min(character_count, 42)
ability = 0
for j in range(union_count):
    char_level = character_levels[j]
    for criterion in union_criteria:
        if char_level < criterion:
            break
        ability += 1
print(f'{sum(character_levels[:union_count])} {ability}')
