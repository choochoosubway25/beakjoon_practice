import sys

'''
주어진 스텝에 대하여 우리가 최대로 이동할 수 있는 거리를 계산하면 다음과 같다.
2 step : 1, 1 -> 2
3 step : 1, 2, 1 -> 4
4 step : 1, 2, 2, 1 -> 6
5 step : 1, 2, 3, 2, 1 -> 9
6 step : 1, 2, 3, 3, 2, 1 -> 12
7 step : 1, 2, 3, 4, 3, 2, 1 -> 16
...
이런 식으로 n step 에 최대로 갈 수 있는 거리는 sigma^n_{k=1} floor((k+1)/2) 이다.
이를 이용하여 주어진 거리에 필요한 최소한의 이동 횟수를 구할 수 있다.
'''
test_count = int(sys.stdin.readline())
for _ in range(test_count):
    x, y = map(int, sys.stdin.readline().split())
    dist = y - x
    s = 1
    step = 1
    while dist > s:
        step += 1
        s += (step + 1) // 2
    print(step)
