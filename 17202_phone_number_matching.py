import sys

phone_number_1 = str(sys.stdin.readline().strip())
phone_number_2 = str(sys.stdin.readline().strip())
combined_list = list()
for _ in range(8):
    combined_list.append(int(phone_number_1[_]))
    combined_list.append(int(phone_number_2[_]))
for i in range(14):
    new_combined_list = list()
    for j in range(len(combined_list) - 1):
        new_value = (combined_list[j] + combined_list[j + 1]) % 10
        new_combined_list.append(new_value)
    combined_list = new_combined_list
print(f'{combined_list[0]}{combined_list[1]}')
