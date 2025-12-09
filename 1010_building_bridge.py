import sys


def n_choose_m(n: int, m: int) -> int:
    n = min(n, m-n)
    result = 1
    for i in range(n):
        result *= (m-i)
        result //= (i+1)
    return result


test_count = int(sys.stdin.readline())
for _ in range(test_count):
    n_1, m_1 = map(int, sys.stdin.readline().split())
    print(n_choose_m(n_1, m_1))
