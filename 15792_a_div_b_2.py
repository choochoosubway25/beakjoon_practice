a, b = map(int, input().split())

result = str()
result += f"{a//b}."
for i in range(1000):
    a = a % b
    a = 10 * a
    result += f"{a//b}"
print(result)