import sys

line_count = int(sys.stdin.readline())
numbers = list()
num_char = ""
for i in range(line_count):
    inputs = sys.stdin.readline().strip()
    for char in inputs:
        if 48 <= ord(char) <= 57:
            num_char += char
        else:
            if num_char != "":
                numbers.append(int(num_char))
                num_char = ""
    if num_char != "":
        numbers.append(int(num_char))
        num_char = ""
numbers.sort()
for num in numbers:
    print(num)
