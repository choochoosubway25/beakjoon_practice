import sys

'''
이 문제에서 행성계를 진입/이탈 할 수 밖에 없는 조건은 다음과 같다.
시작점 혹은 도착점이 행성계 안에 있는 경우.
단 시작점과 도착점이 둘 다 안에 있는 경우는 진입 이탈 할 필요가 없으니 이런 경우는 제외 한다.
이는 시작점(혹은 도착점) 과 행성계 중심과의 거리가 행성계 경계의 거리보다 작을 경우와 같다.
'''
test_cases = int(sys.stdin.readline())
for _ in range(test_cases):
    # 시작점, 도착점의 좌표 받기
    start_x, start_y, end_x, end_y = map(int, sys.stdin.readline().split())
    planet_count = int(sys.stdin.readline())
    # 시작점, 도착점을 둘러싼 행성계를 세는 변수를 선언.
    covered_start_only, covered_end_only = 0, 0
    for i in range(planet_count):
        x, y, r = map(int, sys.stdin.readline().split())
        distance_squared_start = (x - start_x) ** 2 + (y - start_y) ** 2
        distance_squared_end = (x - end_x) ** 2 + (y - end_y) ** 2
        # 시작점(도착점)과 행성계 경계가 걸친 경우(거리가 같음)는 없으므로 등호는 빼도 된다.
        start_covered = distance_squared_start < r ** 2
        end_covered = distance_squared_end < r ** 2
        # 시작점과 도착점이 같이 둘러싸인 경우에는 아래 if구문이 작동하지 않아 카운트 되지 않는다.
        if start_covered and not end_covered:
            covered_start_only += 1
        if end_covered and not start_covered:
            covered_end_only += 1
    # 문제 조건에 따라 행성계 끼리 서로 겹치는 경우는 없으므로 시작점, 도착점을 둘러싼 행성계의 개수를 더하면 된다.
    print(covered_start_only + covered_end_only)
