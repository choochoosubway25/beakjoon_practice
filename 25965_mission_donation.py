import sys

n = int(sys.stdin.readline())
for _ in range(n):
    total_amount = 0
    mission_num = int(sys.stdin.readline())
    mission_list = list()
    for _ in range(mission_num):
        k_amount, d_amount, a_amount = map(int, sys.stdin.readline().split())
        mission_list.append((k_amount, d_amount, a_amount))
    k, d, a = map(int, sys.stdin.readline().split())
    for mission in mission_list:
        donate_amount = k * mission[0] - d * mission[1] + a * mission[2]
        if donate_amount > 0:
            total_amount += donate_amount
    print(total_amount)
