A, B, C = map(int, input().split())

result = -1
if C - B <= 0:
    result = -1
else:
    result = (A // (C - B)) + 1
print(result)