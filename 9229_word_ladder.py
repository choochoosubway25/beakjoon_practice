import sys

word_list = list()
while True:
    words = sys.stdin.readline().strip()
    if words != "#":
        word_list.append(words)
    else:
        if len(word_list) == 0:
            break
        for i in range(1, len(word_list)):
            before_word, after_word = word_list[i - 1], word_list[i]
            length_same = len(before_word) == len(after_word)
            if not length_same:
                print('Incorrect')
                break
            difference_count = 0
            for j in range(len(before_word)):
                if before_word[j] != after_word[j]:
                    difference_count += 1
            if difference_count != 1:
                print('Incorrect')
                break
        else: # looping success listener
            print('Correct')
        word_list = list()
