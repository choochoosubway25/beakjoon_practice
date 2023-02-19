a = int(input())
b = int(input())
c = int(input())
result = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
number = a * b * c
while number > 0:
    digit = number % 10
    result[digit] += 1
    number = number // 10
for count in result:
    print(count)