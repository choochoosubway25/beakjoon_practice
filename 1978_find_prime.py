n = int(input())
num_list = list(map(int, input().split()))
prime_count = 0
for num in num_list:
    is_prime = 1
    if num == 1:
        is_prime = 0
    i = 2
    while i * i <= num:
        if num % i == 0:
            is_prime = 0
            break
        i += 1
    prime_count += is_prime
print(prime_count)