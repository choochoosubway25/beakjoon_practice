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


m = int(input())
n = int(input())
least_prime = -1
sum_prime = 0
for num in range(m, n+1):
    if is_prime(num):
        if least_prime < 0:
            least_prime = num
        sum_prime += num
if least_prime < 0:
    print(least_prime)
else:
    print(sum_prime)
    print(least_prime)
