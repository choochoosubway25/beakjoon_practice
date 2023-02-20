def is_prime(num: int) -> bool:
    result = True
    if num == 1:
        result = False
    i = 2
    while i * i <= num:
        if num % i == 0:
            result = False
            break
        i += 1
    return result


m, n = map(int, input().split())
least_prime = -1
sum_prime = 0
for num in range(m, n+1):
    if is_prime(num):
        print(num)

