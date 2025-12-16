import sys

test_count = int(sys.stdin.readline())
for _ in range(test_count):
    total, index = map(int, sys.stdin.readline().split())
    printing_queue = list()
    priorities = list(map(int, sys.stdin.readline().split()))
    for i in range(total):
        printing_queue.append((i, priorities[i]))
    for j in range(total):
        max_priority = max(priorities)
        output = None
        for k in range(total):
            temp = printing_queue.pop(0)
            if temp[1] == max_priority:
                output = temp
                priorities.remove(max_priority)
                break
            else:
                printing_queue.append(temp)
        if output[0] == index:
            print(j + 1)
            break
