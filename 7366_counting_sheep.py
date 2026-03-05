import sys

test_count = int(sys.stdin.readline())
for _ in range(test_count):
    word_count = int(sys.stdin.readline())
    sheep_string = sys.stdin.readline().strip().split()
    sheep_count = sheep_string.count("sheep")
    print(f"Case {_+1}: This list contains {sheep_count} sheep.\n")