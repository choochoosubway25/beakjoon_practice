import sys

length = int(sys.stdin.readline())
paper = [[] for j in range(length)]
for i in range(length):
    paper[i] = list(map(int, sys.stdin.readline().split()))
black = 0
white = 0
invest_size = 1
while invest_size < length:
    for k1 in range(0, length, 2*invest_size):
        for k2 in range(0, length, 2*invest_size):
            a, b = paper[k1][k2:k2+2*invest_size:invest_size]
            c, d = paper[k1+invest_size][k2:k2+2*invest_size:invest_size]
            if a != b or b != c or c != d:
                white += (a == 0) + (b == 0) + (c == 0) + (d == 0)
                black += (a == 1) + (b == 1) + (c == 1) + (d == 1)
                paper[k1][k2] = -1
    invest_size *= 2
white += (paper[0][0] == 0)
black += (paper[0][0] == 1)
print(white)
print(black)
