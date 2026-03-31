import sys


primes = [2, 3, 5, 7]
while True:
    try:
        limits, length = map(int, sys.stdin.readline().split())
    except EOFError:
        break
    except ValueError:
        break
    prime_list = [1]
    prime_max = max(primes)
    for i in range(2, limits + 1):
        if i in primes:
            prime_list.append(i)
        else:
            for prime in primes:
                if i % prime == 0:
                    break
            else:
                primes.append(i)
                prime_list.append(i)
    center = len(prime_list) // 2
    start = center - length
    end = min(center + length, len(prime_list) + 1)
    if (len(prime_list) % 2) != 0:
        start += 1
    result = ' '.join(map(str, prime_list[start:end]))
    print(f"{limits} {length}: {result}\n")
