import sys


def joint_position(cor_1: (int, int, int), cor_2: (int, int, int)) -> int:
    # 둘의 위치가 같을 경우
    if cor_1[0] == cor_2[0] and cor_1[1] == cor_2[1]:
        # 둘의 거리가 둘 다 0이라면 가능한 점은 1개뿐이다.
        if cor_1[2] == 0 and cor_2[2] == 0:
            result = 1
        # 만약 둘의 거리가 0이 아닐 때, 두 값이 다른 값이면 값은 0, 서로 같으면 원래 값은 무한대다.
        elif cor_1[2] != cor_2[2]:
            result = 0
        else:
            result = -1
    # 둘의 위치가 다를 경우
    else:
        # 둘의 위치간 거리를 좌표계를 이용해 구한다. 이 때, 정수형 상태에서의 비교를 위해 거리의 제곱값을 저장한다.
        points_distance_squared = (cor_1[0] - cor_2[0]) ** 2 + (cor_1[1] - cor_2[1]) ** 2
        # 둘에게 주어진 탐사 거리를 탐사 거리의 합을 구한다. 둘의 위치간 거리의 값과의 비교를 위해, 제곱하여 저장한다.
        given_distance_out_squared = (cor_1[2] + cor_2[2]) ** 2
        # 둘에게 주어진 탐사 거리를 탐사 거리의 차을 구한다. 둘의 위치간 거리의 값과의 비교를 위해, 제곱하여 저장한다.
        given_distance_in_squared = (cor_1[2] - cor_2[2]) ** 2
        # 위치간 길이 > 탐사거리의 합 -> 각자 주어진 거리로 원을 그리면 접점이 0개
        if points_distance_squared > given_distance_out_squared:
            result = 0
        # 위치간 길이 < 탐사거리의 합 -> 각자 주어진 거리로 원을 그리면 접점이 2개
        elif points_distance_squared < given_distance_out_squared:
            # 위치간 길이 > 탐사 거리의 차 -> 접점이 2개
            if points_distance_squared > given_distance_in_squared:
                result = 2
            elif points_distance_squared < given_distance_in_squared:
                result = 0
            else:
                result = 1
        # 위치간 길이 = 탐사거리의 합 -> 각자 주어진 거리로 원을 그리면 접점이 1개
        else:
            result = 1
    return result


test_count = int(sys.stdin.readline())
for _ in range(test_count):
    x_1, y_1, r_1, x_2, y_2, r_2 = map(int, sys.stdin.readline().split())
    print(joint_position((x_1, y_1, r_1), (x_2, y_2, r_2)))
