import sys

word = str(sys.stdin.readline().strip())
char_list = ['K', 'O', 'R', 'E', 'A']
result = 0
char_index = 0
for char in word:
    if char == char_list[char_index]:
        result += 1
        char_index = (char_index + 1) % 5
print(result)
