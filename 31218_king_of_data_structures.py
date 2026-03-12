import sys


# 잔디밭을 저장한다. 이 때, 큰 값의 n,m에 대응하기 위해 dict[int, set[int]] 형으로 저장한다.
rows, columns, query_count = map(int, sys.stdin.readline().split())
lawns_dict = {}
total_lawn = rows * columns
for row in range(rows):
    lawns_row = set([_ + 1 for _ in range(columns)])
    lawns_dict[row + 1] = lawns_row
# 쿼리구문을 처리합니다.
for query_num in range(query_count):
    query_input = sys.stdin.readline().split() # 시간 절약을 위해 int형 변환은 쿼리 처리 단계에서 합니다.
    # 각자의 쿼리는 맨 앞에 쿼리의 종류를 나타내므로 맨 앞의 숫자를 비교합니다.
    # 1번 쿼리 처리 로직
    if query_input[0] == "1":
        dy, dx, y, x = map(int, query_input[1:])
        while True:
            if x in lawns_dict[y]:
                lawns_dict[y].remove(x)
                total_lawn -= 1
            else:
                break
            is_y_go_in_bound = 1 <= y + dy <= rows
            is_x_go_in_bound = 1 <= x + dx <= columns
            if not is_y_go_in_bound or not is_x_go_in_bound:
                break
            y = y + dy
            x = x + dx

    # 2번 쿼리 처리 로직
    elif query_input[0] == "2":
        y, x = map(int, query_input[1:])
        if x in lawns_dict[y]:
            print(0)
        else:
            print(1)

    # 3번 쿼리 처리 로직
    elif query_input[0] == "3":
        print(total_lawn)
