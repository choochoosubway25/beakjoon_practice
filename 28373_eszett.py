import sys


input_word = sys.stdin.readline().strip()
s_interval_list = list()
i = 0
start = -1
end = -1
s_start = False
while i < len(input_word):
    alphabet = input_word[i]
    if alphabet == "S" and not s_start:
        s_start = True
        start = i
    elif alphabet != "S" and s_start:
        s_start = False
        end = i
        s_interval_list.append([start, end])
    i += 1
else: # while 구문 종료시
    if s_start:
        end = i
        s_interval_list.append([start, end])
case_count = 1
for start, end in s_interval_list:
    if end - start == 1:
        case_count *= 1
    if end - start == 2:
        case_count *= 2
    if end - start == 3:
        case_count *= 3
if case_count > 1:
    word_case = []
    for start, end in s_interval_list:
        if end - start == 2:
            word_case.append((input_word[:start]).lower() + "ss" + (input_word[end:]).lower())
            word_case.append((input_word[:start]).lower() + "B" + (input_word[end:]).lower())
        elif end - start == 3:
            word_case.append((input_word[:start]).lower() + "sss" + (input_word[end:]).lower())
            word_case.append((input_word[:start]).lower() + "sB" + (input_word[end:]).lower())
            word_case.append((input_word[:start]).lower() + "Bs" + (input_word[end:]).lower())
    for word in word_case:
        print(word)
else:
    print(input_word.lower())