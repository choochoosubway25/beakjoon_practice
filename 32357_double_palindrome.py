import sys

strings_count = int(sys.stdin.readline())
palindrome_count = 0
for _ in range(strings_count):
    word = str(sys.stdin.readline().strip())
    for i in range(len(word) // 2):
        if word[i] != word[-i-1]:
            break
    else:
        palindrome_count += 1
print(palindrome_count * (palindrome_count - 1))
