import sys

num_iter = int(sys.stdin.readline())
for _ in range(num_iter):
    result = 'YES'
    brackets = list()
    strings = str(sys.stdin.readline())
    strings = strings[:-1]
    for char in strings:
        if char == '(':
            brackets.append(char)
        if char == ')':
            if len(brackets) == 0:
                result = 'NO'
                break
            else:
                bracket = brackets.pop()
                is_coupled = (bracket == '(' and char == ')')
                if not is_coupled:
                    result = 'NO'
                    break
    if len(brackets) != 0:
        result = 'NO'
    print(result)

