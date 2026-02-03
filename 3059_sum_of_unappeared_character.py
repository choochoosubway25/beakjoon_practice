import sys

test_count = int(sys.stdin.readline())
sum_of_total = (90 * 91 // 2) - (64 * 65 // 2)
for _ in range(test_count):
    sum_of_appeared = 0
    character_set = set()
    character_input = sys.stdin.readline().strip()
    for char in character_input:
        character_set.add(char)
    for char in character_set:
        sum_of_appeared += ord(char)
    print(sum_of_total - sum_of_appeared)
