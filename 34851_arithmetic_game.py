import sys

number_count = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
result = 0
if numbers[0] == 1 or numbers[1] == 1:
    result = (numbers[0] + numbers[1]) % 1000000007
else:
    result = (numbers[0] * numbers[1]) % 1000000007
for i in range(1, number_count):
    number = numbers[i + 1]
    if number == 1:
        result += 1
        result %= 1000000007
    else:
        result *= number
        result %= 1000000007
print(result)
