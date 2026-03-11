import sys

# 입력값 받아오기
start_position, frog_count = map(int, sys.stdin.readline().split())
frog_positions = list(map(int, sys.stdin.readline().split()))
jump_distance, walking_cost = map(int, sys.stdin.readline().split())
# 각 개구리를 만나기 위한 체력 소모 변수 선언
power_consumptions = [-1 for _ in range(frog_count)]
# 각 개구리의 체력 소모 양 계산.
for i in range(frog_count):
    consumption = 0
    distance = abs(start_position - frog_positions[i])
    # 만약 두 개구리가 K만큼 점프할 수 있다면, 그 만큼 거리를 뺀 나머지에 걷기에 소모되는 체력을 곱하여 체력소모 계산
    if distance >= 2 * jump_distance:
        distance -= 2 * jump_distance
        consumption += walking_cost * distance
    # 아니라면 L의 값과 상관없이 K보다 작은 만큼 점프하는 것이 체력 소모가 적으므로 그 만큼의 값을 계산.
    elif distance != 0: # 단 거리가 0이면 이미 만난 것이므로 이 계산에서 제외한다.
        consumption += 2 * jump_distance - distance
    power_consumptions[i] = consumption
lower_consumption = min(power_consumptions)
lower_index = power_consumptions.index(lower_consumption)
print(f"{lower_consumption} {lower_index + 1}")
