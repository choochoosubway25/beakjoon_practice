import sys

number_count, target_number = map(int, sys.stdin.readline().split())
number_list = list(map(int, sys.stdin.readline().split()))
result = 0
for i in range(number_count):
    if target_number - number_list[i] in number_list:
        result += 1
print(result // 2)
