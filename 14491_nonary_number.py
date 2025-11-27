import sys

result = str()
target = int(sys.stdin.readline())

while target > 0:
    result = str(target % 9) + result
    target = target // 9

print(result)
