import sys



nautilus_sequence = [0, 1, 2, 3]
nautilus_maximum = 3
snail_count = int(sys.stdin.readline())
for _ in range(snail_count):
    is_nautilus = False
    patterns = list(map(int, sys.stdin.readline().split()))
    pattern_max = max(patterns)
    while nautilus_maximum < pattern_max:
        new_nautilus_value = sum(nautilus_sequence[-4:])
        nautilus_sequence.append(new_nautilus_value)
        nautilus_maximum = new_nautilus_value
    pattern_length = len(patterns)
    if pattern_length <= len(nautilus_sequence):
        for i in range(pattern_length):
            if patterns[i] != nautilus_sequence[i]:
                break
        else:
            is_nautilus = True
    if is_nautilus:
        print("NAUTILUS")
    else:
        print("SNAIL")