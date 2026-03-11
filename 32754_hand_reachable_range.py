import sys
import math

'''
풀이 과정 :
1) 물체의 무게중심을 구하고 무게중심의 거리를 구한다.
2) 무게중심의 거리와 (무게중심에서 전자기기 모서리 거리 + 손의 거리)값을 비교한다.
 -> 무게중심의 거리가 더 길면 회전해도 닿지 않음 그 외에는 회전하면 닿음.
'''

rectangle_count, hand_range = map(int, sys.stdin.readline().split())
result = 0
for _ in range(rectangle_count):
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, sys.stdin.readline().split())
    center_x, center_y = (x1 + x2 + x3 + x4) / 4, (y1 + y2 + y3 + y4) / 4
    center_edge_distance = math.sqrt((x1 - center_x) ** 2 + (y1 - center_y) ** 2)
    center_origin_distance = math.sqrt(center_x ** 2 + center_y ** 2)
    if center_edge_distance + hand_range >= center_origin_distance:
        result += 1
print(result)
