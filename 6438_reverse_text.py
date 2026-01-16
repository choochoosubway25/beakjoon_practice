import sys

line_count = int(sys.stdin.readline())
for _ in range(line_count):
    texts = str(sys.stdin.readline().strip())
    reverse_text = ''
    for char in texts:
        reverse_text = char + reverse_text
    print(reverse_text)
