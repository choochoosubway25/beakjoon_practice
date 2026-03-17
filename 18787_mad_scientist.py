import sys


string_length = int(sys.stdin.readline())
target_string = sys.stdin.readline().strip()
current_string = sys.stdin.readline().strip()
compare_list = [0 for i in range(string_length)]
for i in range(string_length):
    if current_string[i] != target_string[i]:
        compare_list[i] = 1
compare_string = ''.join(map(str, compare_list))
new_string = compare_string.split("0")
result = 0
for word in new_string:
    if word != "":
        result += 1
print(result)