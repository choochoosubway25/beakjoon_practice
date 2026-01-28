import sys

test_count = int(sys.stdin.readline())
vowel_set = {'a', 'e', 'i', 'o', 'u'}
for i in range(test_count):
    country_name = str(sys.stdin.readline().strip())
    result = ''
    if country_name[-1].lower() in vowel_set:
        result += 'a queen'
    elif country_name[-1].lower() == 'y':
        result += 'nobody'
    else:
        result += 'a king'
    print(f'Case #{i+1}: {country_name} is ruled by {result}.')

