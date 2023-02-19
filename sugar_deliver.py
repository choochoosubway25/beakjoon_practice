impossible_list = [1, 2, 4, 7]

n = int(input())
result = 0
if n in impossible_list:
    result = -1
else:
    five = 0
    three = 0
    five = n // 5
    k = n % 5
    three = k // 3
    while k % 3 != 0:
        five -= 1
        k += 5
        three = k // 3
    result = five + three
print(result)