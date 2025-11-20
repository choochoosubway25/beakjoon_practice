# python의 chr 함수를 이용하여 알파벳에 해당하는 ascii값을 dictionary로 부여한다.
digit_dict = dict()
for _ in range(10):
    digit_dict[_] = str(_)
for _ in range(10, 36):
    digit_dict[_] = chr(_+55)
number, digit_size = map(int, input().split())

digit_result = str()
while number != 0:
    digit = number % digit_size
    digit_result = digit_dict[digit] + digit_result
    number = number // digit_size
print(digit_result)