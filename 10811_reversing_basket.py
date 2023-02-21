n, m = map(int, input().split())

baskets = [i + 1 for i in range(n)]
for m in range(m):
    k1, k2 = map(int, input().split())
    new_list = []
    for j in range(k2 - 1, k1 - 2, -1):
        new_list.append(baskets[j])
    baskets[k1 - 1:k2] = new_list
result = ''
for k in baskets:
    result += str(k)
    result += ' '
print(result[:-1])