def group_word_checker(word:str) -> int:
    result = 1
    char_list = list()
    for char in word:
        if char not in char_list:
            char_list.append(char)
        if char in char_list[:-1]:
            result -= 1
            break
    return result

num = int(input())
group_word_num = 0
for i in range(num):
    word = str(input())
    group_word_num += group_word_checker(word)
print(group_word_num)