word = str(input())

word_leng = len(word)
i = 0
alpha_count = 0
while i < word_leng:
    char = word[i]
    i_count = 1
    if char == 'c' and i + 1 < word_leng:
        if word[i+1] == '=' or word[i+1] == '-':
            i_count += 1
    if char == 'd' and i + 1 < word_leng:
        if word[i+1] == 'z' and i + 2 < word_leng:
            if word[i+2] == '=':
                i_count += 2
        if word[i+1] == '-':
            i_count += 1
    if char == 'l' and i + 1 < word_leng:
        if word[i + 1] == 'j':
            i_count += 1
    if char == 'n' and i + 1 < word_leng:
        if word[i + 1] == 'j':
            i_count += 1
    if char == 's' and i + 1 < word_leng:
        if word[i + 1] == '=':
            i_count += 1
    if char == 'z' and i + 1 < word_leng:
        if word[i + 1] == '=':
            i_count += 1
    alpha_count += 1
    i += i_count

print(alpha_count)