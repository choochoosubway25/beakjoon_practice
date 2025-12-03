import sys


left_bracket = ['(', '[']
right_bracket = [')', ']']
while True:
    result = 'yes'
    brackets = list()
    strings = str(sys.stdin.readline())
    strings = strings[:-1]
    if strings == '.':
        break
    for char in strings:
        if char in left_bracket:
            brackets.append(char)
        if char in right_bracket:
            if len(brackets) == 0:
                result = 'no'
                break
            else:
                bracket = brackets.pop()
                is_small_coupled = (bracket == '(' and char == ')')
                is_big_coupled = (bracket == '[' and char == ']')
                is_coupled = is_big_coupled or is_small_coupled
                if not is_coupled:
                    result = 'no'
                    break
    if len(brackets) != 0:
        result = 'no'
    print(result)
