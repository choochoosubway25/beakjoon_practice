def count_prime(n: int) -> int:
    """
    based on Sieve of Sundaram, link : https://www.baeldung.com/cs/prime-number-algorithms
    :param num: arbitrary number for checking prime
    :return: boolean value of num is prime
    """
    k = (n-1) // 2
    a = [1 for _ in range(k+1)]
    i = 1
    while i*i <= k:
        j = i
        while (i + j + 2*i*j <= k):
            a[i + j + 2*i*j - 1] = 0
            j += 1
        i += 1
    return sum(a)


for i in range(1, 20):
    print(i, count_prime(i))