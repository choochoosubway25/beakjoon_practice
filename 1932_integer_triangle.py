import sys

size_num = int(sys.stdin.readline())
given_list = list()
for _ in range(size_num):
    int_list = list(map(int, sys.stdin.readline().split()))
    given_list.append(int_list)
# 밑에서부터 부분합이 큰 쪽을 저장한다.
for i in range(size_num-1, -1, -1):
    # i-1행에 있는 열에 대해 밑에 있는 두 값의 값을 비교 후, 더 큰값을 미리 더해 저장한다.
    for j in range(i):
        if given_list[i][j] > given_list[i][j+1]:
            given_list[i-1][j] += given_list[i][j]
        else:
            given_list[i-1][j] += given_list[i][j+1]
print(given_list[0][0])
