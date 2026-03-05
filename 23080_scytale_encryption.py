import sys

thickness = int(sys.stdin.readline())
encrypted_string = sys.stdin.readline().strip()
length = len(encrypted_string)
char_list = list()
for i in range(0, length, thickness):
    char_list.append(encrypted_string[i])
print(''.join(char_list))
