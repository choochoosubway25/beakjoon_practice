def factorial(num):
    if num < 1:
        return 1
    else:
        return num*factorial(num-1)


t = int(input())
for i in range(t):
    k = int(input())
    n = int(input())
    print(factorial(n+k)//(factorial(n-1)*factorial(k+1)))
