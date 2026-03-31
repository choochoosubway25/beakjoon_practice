import sys


'''
참고 사항:
각도를 k 라디안 만큼 돌릴 경우, 대응되는 mapping(행렬)은 다음과 같다.
f = [[ cos k, -sin k ],
     [ sin k , cos k ]]
따라서 왼쪽으로 90도 돌리면 행렬은
f = [[ 0, -1 ],
     [ 1,  0 ]]
오른쪽으로 돌리면 행렬은
f = [[  0, 1 ],
     [ -1, 0 ]]
'''
turning_count, walked_distance = map(int, sys.stdin.readline().split())
arrow_states = [1, 0]
result_coordinate = [0, 0]
start_point = 0
final_point = walked_distance
for _ in range(turning_count):
    turning_info = sys.stdin.readline().split()
    end_point = int(turning_info[0])
    walking_distance = end_point - start_point
    result_coordinate[0] += arrow_states[0] * walking_distance
    result_coordinate[1] += arrow_states[1] * walking_distance
    if turning_info[1] == 'right':
        arrow_states[0], arrow_states[1] = arrow_states[1], -arrow_states[0]
    else:
        arrow_states[0], arrow_states[1] = -arrow_states[1], arrow_states[0]
    start_point = end_point
else:
    result_coordinate[0] += arrow_states[0] * (final_point - start_point)
    result_coordinate[1] += arrow_states[1] * (final_point - start_point)

print(' '.join(map(str, result_coordinate)))