import sys


test_count = int(sys.stdin.readline())
for _ in range(test_count):
    children_count = int(sys.stdin.readline())
    children_list = list(map(int, sys.stdin.readline().split()))
    turns = 0
    while True:
        # 홀수인 아이에게 사탕 보충
        for i in range(children_count):
            child = children_list[i]
            if child % 2 != 0:
                children_list[i] = child + 1
        # 사탕 개수가 모두 같은지 확인
        child_1 = children_list[0]
        for child in children_list[1:]:
            if child != child_1:
                break
        else: # 모두 같은 사탕을 가지면
            print(turns)
            break
        turns = turns + 1
        new_list = [0 for _ in range(children_count)]
        for i in range(len(children_list)):
            if i == children_count-1:
                new_list[0] = children_list[i] // 2
                children_list[i] = children_list[i] // 2
            else:
                new_list[i+1] = children_list[i] // 2
                children_list[i] = children_list[i] // 2
        for i in range(len(children_list)):
            children_list[i] = children_list[i] + new_list[i]
