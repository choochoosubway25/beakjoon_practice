import sys

n = int(sys.stdin.readline())
data_list = list()
average = 0
count_dict = dict()
count_max = 0
maximum = 0
minimum = 0
for i in range(n):
    data = int(sys.stdin.readline())
    data_list.append(data)
    # 재귀적으로 평균을 구하는 방법 사용(시간 절약)
    average = (i/(i+1)) * average + (1/(i+1)) * data
    # 데이터의 빈도수를 사전형 자료를 이용해 기록
    if data in count_dict.keys():
        count_dict[data] += 1
    else:
        count_dict[data] = 1
    if count_dict[data] > count_max:
        count_max = count_dict[data]
    # 최대값, 최소값 갱신
    if i == 0:
        maximum = data
        minimum = data
        continue
    if maximum < data:
        maximum = data
    if minimum > data:
        minimum = data
data_list.sort()
median = data_list[n // 2]
mean_list = list()
for number, count in count_dict.items():
    if count == count_max:
        mean_list.append(number)
mean_list.sort()
try:
    mean = mean_list[1]
except IndexError:
    mean = mean_list[0]
print(round(average))
print(median)
print(mean)
print(maximum - minimum)
