import sys

n, target = map(int, sys.stdin.readline().split())
coin_list = list()
result = 0
for _ in range(n):
    value = int(sys.stdin.readline())
    coin_list.append(value)
for i in range(n-1, -1, -1):
    coin = coin_list[i]
    result += (target // coin)
    target = target % coin
print(result)
