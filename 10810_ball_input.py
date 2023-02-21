n, m = map(int, input().split())

baskets = [0 for _ in range(n)]
for j in range(m):
    start, end, num = map(int, input().split())
    for i in range(start-1, end):
        baskets[i] = num
result = ''
for k in baskets:
    result += str(k)
    result += ' '
print(result[:-1])
