import sys
import math


def pay_function(x, painter_efficients, day_penalties, painter_rates):
    return painter_rates * x + (painter_efficients * day_penalties / x)


painter_efficient, day_penalty, painter_rate = map(int, sys.stdin.readline().split())
optimal_point = math.sqrt(day_penalty * painter_efficient / painter_rate)
neighbourhood = list()
if int(optimal_point) - 1 > 0:
    neighbourhood.append(int(optimal_point) - 1)
if int(optimal_point) >= 1:
    neighbourhood.append(int(optimal_point))
neighbourhood = neighbourhood + [int(optimal_point + 1)]
function_value = [pay_function(y, painter_efficient, day_penalty, painter_rate) for y in neighbourhood]
result = min(function_value)
print(f'{result:0.3f}')
