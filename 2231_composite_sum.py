def digit_sum(n: int) -> int:
    result = 0
    if n < 0:
        return result
    while n > 0:
        result += n % 10
        n = n // 10
    return result


def decomposition_sum(n: int) -> int:
    return n + digit_sum(n)


def find_generator(n: int) -> int:
    result = 0
    for i in range(1, n+1):
        de_sum = decomposition_sum(i)
        if de_sum == n:
            result = i
            break
    return result


n = int(input())
print(find_generator(n))
