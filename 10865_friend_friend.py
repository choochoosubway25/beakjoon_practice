import sys

n, m = map(int, sys.stdin.readline().split())
friend_num_list = [0 for _ in range(n)]
for _ in range(m):
    num_1, num_2 = map(int, sys.stdin.readline().split())
    friend_num_list[num_1-1] += 1
    friend_num_list[num_2-1] += 1
for num in friend_num_list:
    print(num)
