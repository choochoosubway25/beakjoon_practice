t = int(input())
for i in range(t):
    h, w, n = map(int, input().split())
    if (n % h) != 0:
        y = (n % h)
        x = (n // h) + 1
    else:
        y = h
        x = (n // h)
    print('{0:d}{1:02d}'.format(y, x))