def z_num(n: int, r: int, c: int) -> int:
    if n < 1:
        return 0
    if n == 1:
        return 2*r+1*c
    else:
        rescale = 2 ** (n - 1)
        posnum = (2 * (r // rescale) + c // rescale)
        return (rescale ** 2) * posnum + z_num(n - 1, r % rescale, c % rescale)


size, row, column = map(int, input().split())
print(z_num(size, row, column))
