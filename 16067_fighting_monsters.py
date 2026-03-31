import sys
from bisect import bisect_right
from collections import Counter


'''
풀이 과정 : 
두 몬스터에 대해 선공을 A, 후공을 B라 하자.
A의 초기체력을 a, B의 초기체력을 b라고 하고 전투과정을 무한히 반복하면 다음과 같다.
a / b -> a / b-a -> 2a-b / b-a -> 2a-b / 2b-3a -> 5a-3b / 2b-3a ...
즉, k번 돌아가면서 선공과 후공 모두 공격을 한 뒤의 두 몬스터의 체력은 다음과 같다.
f(2k+1)a-f(2k)b / f(2k-1)b-f(2k)a 
이 때, f(n)은 f(0) = 0, f(1) = 1, f(n+2) = f(n+1) + f(n) (n >= 0)으로 정의되는 피보나치 수열이다.
lemma) 전투가 끝났을 때, 한쪽의 체력이 1이라면 다른쪽의 체력은 0이다.
proof) 전투가 끝났을 경우, 한쪽의 체력이 1일때, 다른쪽의 체력이 x라고 하자. x는 0보다 작거나 같은 정수다.
그렇다면 전투가 끝나기 직전에 사망한 쪽의 체력은 x+1이다. 
그런데 이 경우에는 사망상태가 아니므로 이 때의 체력은 0보다 커야한다. 
즉 x<=0이면서 x+1>0이어야 하는데 이는 -1<x<=0 과 같고, 이를 만족하는 x는 0밖에 없다. q.e.d.
theorem) 전투가 끝났을 때, 한쪽의 체력이 1이 되려면 양쪽의 체력은 각각 f(n), f(n+1)이며
이 경우 선공은 체력이 f(n)인 쪽이어야 한다.
proof) 우선 문제의 경우가 되려면 체력은 1 / x(x<=0)이어야 한다.
그런데 lemma에 따르면 x = 0 이어야 한다.
즉 체력상태는 1 / 0 이라는 것이다.
이제 이를 역산으로 셈을 해보면 다음과 같다.
1 / 0 -> 1 / 1 -> 2 / 1 -> 2 / 3 -> 5 / 3 -> ...
즉 처음 체력상태는 f(1) / f(0) 이고 한번씩 역산하면
f(1) / f(0) + f(1) = f(2) -> f(1) + f(2) = f(3) / f(2) 이렇게 되며
역산을 할 때 마다 f(n) / f(n+1)의 형태가 유지되며, 이 때 체력이 추가 되는 쪽은 f(n) + f(n-1)의 형태가 되어 f(n+1)이 된다.
한편 이렇게 두 몬스터의 체력이 f(n) / f(n+1)인 상황이라고 하자.
만약 f(n+1)이 선공이라면 공격후 체력은 f(n+1) / f(n)-f(n+1)이 된다.
그런데 f(n+1) >= f(n)이므로 f(n)의 체력이 있던 쪽은 사망하게 된다.
이럴 경우, f(n+1) = 1인 경우가 아니라면 문제에서 주어진 경우와는 다르게 된다.
이런 경우는 n = 1인 경우 밖에 없다. 
즉 n >= 2이라면 위 문제와 모순이므로 n >=2일 경우에는 f(n)쪽이 선공이어야 문제 상황에 들어 맞는다.
한면 n = 1일 경우 주어진 체력은 f(2) / f(1) -> 1 / 1 -> f(1) / f(2)이 되어 f(n)쪽이 선공인 상황으로 변환가능하다.
q.e.d
'''

# 몬스터의 정보들을 받아온다.
monster_count = int(sys.stdin.readline())
monster_power_list = list(map(int, sys.stdin.readline().split()))
maximum_power = max(monster_power_list)
fibonacci_list = [0, 1]
# 빠른 계산을 위해 피보나치 항들을 계산해 둔다.
while fibonacci_list[-1] < maximum_power:
    fibonacci_list.append(fibonacci_list[-2] + fibonacci_list[-1])
# 이제 각 몬스터의 체력(power)가 피보나치 항인지 체크한다. 이 때, 피보나치의 몇번째 항인지 기록한다.
# 단 아래 알고리즘을 쉽게 적용하기 위해 값이 1인 경우는 인덱스 값을 2로 저장한다.
index_list = [0 for _ in range(monster_count)]
for t in range(monster_count):
    monster_power = monster_power_list[t]
    index_temp = bisect_right(fibonacci_list, monster_power) - 1
    if monster_power == fibonacci_list[index_temp]:
        index_list[t] = index_temp
# 이제 각 몬스터에 대해 피보나치 인덱스 값이 양수일 경우, 1보다 더 큰 값이 있는지 살펴본다.
index_counter = Counter(index_list)
for index_value in index_counter:
    i, j = -1, -1
    is_found = False
    if index_value == 0:
        continue
    elif index_value == 2:
        if index_counter[index_value] >= 2:
            i = index_list.index(index_value)
            j = index_list.index(index_value, i+1)
            is_found = True
    else:
        if index_counter[index_value + 1] >= 1:
            i = index_list.index(index_value)
            j = index_list.index(index_value + 1)
            is_found = True
    if is_found:
        print(f"{i + 1} {j + 1}")
        break
else:
    print("impossible")
