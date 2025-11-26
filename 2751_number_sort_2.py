import sys

sort_list = list()
iter_num = int(sys.stdin.readline())

for i in range(iter_num):
    number = int(sys.stdin.readline())
    sort_list.append(number)
sort_list.sort()
for num in sort_list:
    print(num)
