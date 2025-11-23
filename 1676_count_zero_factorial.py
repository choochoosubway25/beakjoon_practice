n = int(input())
mul = 1
zero_num = 0
for i in range(n):
    mul = mul*(i+1)
    while mul % 10 == 0:
        mul = mul // 10
        zero_num += 1
print(zero_num)