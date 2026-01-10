import sys
import heapq

test_count = int(sys.stdin.readline())
for _ in range(test_count):
    houses, budget = map(int, sys.stdin.readline().split())
    houses_list = [0 for i in range(houses)]
    houses_price = list(map(int, sys.stdin.readline().split()))
    heapq.heapify(houses_price)
    spends = 0
    house_count = 0
    while len(houses_price) > 0:
        house_to_buy = heapq.heappop(houses_price)
        spends += house_to_buy
        if spends > budget:
            break
        house_count += 1
    print(f'Case #{_+1}: {house_count}')
