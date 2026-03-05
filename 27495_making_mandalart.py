import sys

target_dict = dict()
final_target = str()
for i in range(3):
    division_1 = list()
    division_2 = list()
    division_3 = list()
    middle_1 = str()
    middle_2 = str()
    middle_3 = str()
    for j in range(3):
        inputs = sys.stdin.readline().split()
        if j == 1:
            division_1 += [inputs[0], inputs[2]]
            division_2 += [inputs[3], inputs[5]]
            division_3 += [inputs[6], inputs[8]]
            middle_1 += inputs[1]
            middle_2 += inputs[4]
            middle_3 += inputs[7]
            if i == 1:
                final_target += inputs[4]
        else:
            division_1 += inputs[0:3]
            division_2 += inputs[3:6]
            division_3 += inputs[6:9]
    target_dict[middle_1] = division_1
    target_dict[middle_2] = division_2
    target_dict[middle_3] = division_3
target_dict[final_target].sort()
for k in range(8):
    middle_target = target_dict[final_target][k]
    target_dict[middle_target].sort()
    print(f"#{k+1}. {middle_target}")
    for k2 in range(8):
        small_target = target_dict[middle_target][k2]
        print(f"#{k+1}-{k2+1}. {small_target}")
