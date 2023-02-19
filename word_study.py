word = str(input())
word = word.upper()
char_dict = dict()
for char in word:
    if char in char_dict:
        char_dict[char] += 1
    else:
        char_dict[char] = 0
maximum_repeat = ''
maximum_count = -1
for char in char_dict.keys():
    if char_dict[char] > maximum_count:
        maximum_repeat = char
        maximum_count = char_dict[char]
    elif char_dict[char] == maximum_count:
        maximum_repeat = "?"
print(maximum_repeat)