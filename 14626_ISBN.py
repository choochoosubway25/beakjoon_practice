ruined_code = str(input())
code_length = 13
ruined_index = -1
restore_number = -1
check_sum = 0

for i in range(code_length):
    if ruined_code[i] == '*':
        ruined_index = i
    else:
        check_sum += (2 * (i % 2) + 1) * int(ruined_code[i])
if ruined_index % 2 == 1:
    restore_number = 7 * (-check_sum) % 10
else:
    restore_number = -check_sum % 10
print(restore_number)
