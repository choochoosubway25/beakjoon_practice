import sys

test_count = int(sys.stdin.readline())
prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
for _ in range(test_count):
    factoring_dict = dict()
    n = int(sys.stdin.readline())
    prime_index = 0
    while n > 1:
        if prime_index < len(prime_list):
            prime = prime_list[prime_index]
        else:
            found_prime = False
            prime = prime_list[-1] + 1
            while not found_prime:
                if prime ** 2 > n:
                    prime = n
                    break
                for p in prime_list:
                    if prime % p == 0:
                        prime += 1
                        continue
                else:
                    found_prime = True
                    prime_list.append(prime)
        if n % prime == 0:
            n = n // prime
            if prime in factoring_dict.keys():
                factoring_dict[prime] += 1
            else:
                factoring_dict[prime] = 1
        else:
            prime_index += 1
    factors = list(factoring_dict.keys())
    factors.sort()
    for fa in factors:
        print(f"{fa} {factoring_dict[fa]}")
