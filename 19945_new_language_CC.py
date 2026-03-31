n = int(input())
bin_n = bin(n & (2 ** 32 - 1))
binary = f"{bin_n[2:]:0>32}"
result = 1
for i in range(32):
    if binary[i] == "1":
        result = 32 - i
        break
print(result)
