rows, columns = map(int, input().split())
A = list()
B = list()
for i in range(rows):
    row = map(int, input().split())
    A.append(list(row))
for i in range(rows):
    row = map(int, input().split())
    B.append(list(row))
for i in range(rows):
    result = ''
    for j in range(columns):
        result += str(A[i][j] + B[i][j])
        result += ' '
    print(result[:-1])

