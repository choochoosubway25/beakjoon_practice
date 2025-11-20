# python의 chr 함수를 이용하여 알파벳에 해당하는 ascii값을 dictionary로 부여한다.
digit_dict = dict()
for i in range(65, 65+26):
    digit_dict[chr(i)] = i-55
for _ in range(10):
    digit_dict[str(_)] = _

number_value = 0

number, digit_size = map(str, input().split())
digit_size = int(digit_size)

digit_value = 1
for digit_num in range(len(number)-1, -1, -1):
    number_value += digit_dict[number[digit_num]] * digit_value
    digit_value *= digit_size

print(number_value)