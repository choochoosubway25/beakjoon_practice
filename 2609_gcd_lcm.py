n, m = map(int, input().split())

r = 0
product = n*m
while m != 0:
    # using euclidean algorithm
    r = n % m
    n, m = m, r
gcd = n
lcm = product // gcd
print(gcd)
print(lcm)
