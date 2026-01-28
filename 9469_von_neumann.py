import sys

case_count = int(sys.stdin.readline())
for _ in range(case_count):
    case_num, rail_length, velocity_a, velocity_b, velocity_fly = sys.stdin.readline().split()
    rail_length = float(rail_length)
    velocity_a = float(velocity_a)
    velocity_b = float(velocity_b)
    velocity_fly = float(velocity_fly)
    result = rail_length / (velocity_a + velocity_b) * velocity_fly
    print(f'{case_num} {result:.6f}')