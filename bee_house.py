n = int(input())

result = 1
i = 1
d = 6
while i < n:
    i += d
    d += 6
    result += 1
print(result)