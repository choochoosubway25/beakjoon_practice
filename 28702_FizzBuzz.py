result = str()
position = int()
word_list: list[str] = ['Fizz', 'Buzz', 'FizzBuzz']
for i in range(3):
    word = str(input())
    if word not in word_list:
        position = int(word) + 3 - i
        break
if position % 3 == 0:
    result += 'Fizz'
if position % 5 == 0:
    result += 'Buzz'
if result == '':
    result = str(position)
print(result)