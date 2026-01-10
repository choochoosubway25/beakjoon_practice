import sys
import math


def find_gcd(a, b):
    if b > a:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a


n = int(sys.stdin.readline())
# find divisibility
det = (n+1) ** 2 + 4 * n * (n+2)
sqrt_det: int = -1
i = 1
sqrt_int = int(math.sqrt(det))
if sqrt_int ** 2 == det:
    sqrt_det = sqrt_int
if sqrt_det < 0:
    print(-1)
else:
    left_num = -(n+1) - sqrt_det
    right_num = -(n+1) + sqrt_det
    left_gcd = find_gcd(abs(left_num), 2*n)
    right_gcd = find_gcd(abs(right_num), 2*n)
    print(f'{2*n // right_gcd} {-right_num // right_gcd} {2*n // left_gcd} {-left_num // left_gcd}')
