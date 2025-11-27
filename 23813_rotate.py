import sys

number = str(sys.stdin.readline()).strip()
rotate = number[-1] + number[:-1]
result = int(number)

while rotate != number:
    result += int(rotate)
    rotate = rotate[-1] + rotate[:-1]

print(result)