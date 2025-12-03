import sys
import math

while True:
    inputs = sys.stdin.readline().split()
    nx = int(inputs[0])
    ny = int(inputs[1])
    w = float(inputs[2])
    break_criteria = (nx == 0) and (ny == 0) and math.isclose(w, 0.0)
    if break_criteria:
        break
    # 가로로 잔디가 깎이지 않은 부분이 있는지 확인
    horizon_list = list(map(float, sys.stdin.readline().split()))
    horizon_list.sort()
    horizon_list.insert(0, 0.0)
    is_horizon_clear = True
    for i in range(nx):
        if horizon_list[i+1] - horizon_list[i] > w:
            is_horizon_clear = False
            break
    if horizon_list[-1] + w/2 < 75.0:
        is_horizon_clear = False
    # 세로로 잔디가 깎이지 않은 부분이 있는지 확인
    vertical_list = list(map(float, sys.stdin.readline().split()))
    vertical_list.sort()
    vertical_list.insert(0, 0.0)
    is_vertical_clear = True
    for i in range(ny):
        if vertical_list[i+1] - vertical_list[i] > w:
            is_vertical_clear = False
            break
    if vertical_list[-1] + w/2 < 100.0:
        is_vertical_clear = False
    if is_vertical_clear and is_horizon_clear:
        print('YES')
    else:
        print('NO')
