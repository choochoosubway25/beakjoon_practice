import sys

num_iter = int(sys.stdin.readline())
num_list = list()
for _ in range(num_iter):
    number = int(sys.stdin.readline())
    if number != 0:
        num_list.append(number)
    elif number == 0 and len(num_list) != 0:
        num_list.pop()
print(sum(num_list))
