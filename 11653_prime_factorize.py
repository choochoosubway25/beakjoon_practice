n = int(input())

if n != 1:
    i = 2
    while n != 1:
        while n % i == 0:
            print(i)
            n = n//i
        i += 1

