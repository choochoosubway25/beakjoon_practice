n, m = map(int, input().split())

baskets = [i+1 for i in range(n)]
for m in range(m):
    k1, k2 = map(int, input().split())
    baskets[k1-1], baskets[k2-1] = baskets[k2-1], baskets[k1-1]
result = ''
for k in baskets:
    result += str(k)
    result += ' '
print(result[:-1])
