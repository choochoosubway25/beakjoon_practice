sentence = str(input())
word_num = 0
before = ' '
for char in sentence:
    if before == ' ' and char != ' ':
        word_num += 1
    before = char
print(word_num)