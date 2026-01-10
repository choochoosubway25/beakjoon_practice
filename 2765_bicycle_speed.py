import sys

PI = 3.1415927
i = 0
while True:
    i += 1
    diameter, rotations, times = map(float, sys.stdin.readline().split())
    rotations = int(rotations)
    if rotations == 0:
        break
    total_distance = PI * diameter * rotations / (5280 * 12)
    average_speed = total_distance * 60 * 60 / times
    total_distance = int(100 * total_distance + 0.5) / 100
    average_speed = int(100 * average_speed + 0.5) / 100
    print(f'Trip #{i}: {total_distance:0.2f} {average_speed:0.2f}')
