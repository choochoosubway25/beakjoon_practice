import sys
from queue import Queue


test_count = int(sys.stdin.readline())
for _ in range(test_count):
    result_count = 0
    width, height, point_count = map(int, sys.stdin.readline().split())
    # 배추가 심어져있는 위치를 set으로 저장
    point_set = set()
    for k in range(point_count):
        x, y = map(int, sys.stdin.readline().split())
        point_set.add((x, y))
    inspect_queue = Queue()
    while len(point_set) > 0:
        # 임의로 하나의 배추 위치를 받는다.
        finding_point = next(iter(point_set))
        # 배추가 심어져있는지 조사할 위치를 조사 목록 큐에 저장한다.
        inspect_queue.put(finding_point)
        # 조사 위치를 받아올 때 마다 결과값을 1씩 더한다. 이는 인접해있는 배추들을 모두 1개의 결과로 처리하기 때문이다.
        result_count += 1
        while inspect_queue.qsize() > 0:
            x, y = inspect_queue.get()
            # 만약 배추가 심어져 있다면 인접해있는 상하좌우 위치를 조사 목록 큐에 넣는다.
            # 설령 음수가 들어가도, 음수가 있는 포인트는 포인트 set에 무조건 없으므로 시간 비효율이라는 점 외에는 문제 없다.
            if (x, y) in point_set:
                # 조사의 중복을 막기위해, 이미 조사한 점들은 포인트 set에서 제외한다.
                point_set.remove((x, y))
                inspect_queue.put((x+1, y))
                inspect_queue.put((x-1, y))
                inspect_queue.put((x, y+1))
                inspect_queue.put((x, y-1))
    print(result_count)
