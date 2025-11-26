iter_num = int(input())
human_list = list()
result = ''
for i in range(iter_num):
    x, y = map(int, input().split())
    human_list.append((x, y))

for i in range(iter_num):
    rank = 0
    for j in range(iter_num):
        if i == j:
            continue
        if human_list[i][0] < human_list[j][0] and human_list[i][1] < human_list[j][1]:
            rank += 1
    result += str(f'{rank+1} ')
print(result[:-1])
