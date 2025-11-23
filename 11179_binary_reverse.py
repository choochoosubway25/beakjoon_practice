n = int(input())
bin_string = bin(n)[2:]
print(int(bin_string[::-1], 2))
