import sys

vowel_list = ['a', 'e', 'i', 'o', 'u']
test_count = int(sys.stdin.readline())
for _ in range(test_count):
    word = str(sys.stdin.readline().strip())
    vowel_count = 0
    for char in word:
        if char in vowel_list:
            vowel_count += 1
    print(f'The number of vowels in {word} is {vowel_count}.')
