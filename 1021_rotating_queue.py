import sys


'''
풀이과정 : 
이 문제에서 핵심은 뽑아내려고 하는 수에 도달하기 위한 '왼쪽 회전'과 '오른쪽 회전'의 개수를 세는 것이다.
우선, 첫번째 원소를 뽑는 연산의 경우, 추출하는 원소 기준으로 인덱스가 큰 값들의 경우는 
추출 후 연결관계 기준으로 실질적인 인덱스가 실질적으로 1씩 감소한다. 
(ex: 3 4 5 1 2 -> 4 5 1 2. 이 경우에는 1부터 시작해서 인덱스를 다시 매기면 3 4 1 2로 볼 수 있다.)
따라서 주어진 타겟에 대하여 맨 앞부터 값을 뽑은 후, 뒤쪽 값과 비교해서 뒤쪽의 값이 더 크다면 1을 빼는 것을 반복한다.
이렇게 조정이 끝난다면, 조정된 값을 기준으로 거리를 계산한다.
우선 출발 지점이 필요한데, 출발지점은 직전에 추출한 타겟값을 사용한다. 처음에는 1을 쓴다.
그리고 타겟에 도달하기 위해 필요한 왼쪽 회전 연산의 수를 계산한다. 주어진 타겟 값과 직전 타겟값을 비교하여 거리를 구한다.
오른쪽 연산의 경우, 현재 큐 길이만큼 연산하면 제자리로 돌아온다는 것을 이용하여 (현재 큐 길이) - (왼쪽 회전 연산 수)로 구한다.
이 둘을 비교해 최소값을 계속 더해가면 최소값을 구할 수 있다.
'''
initial_queue_length, target_count = map(int, sys.stdin.readline().split())
targets = list(map(int, sys.stdin.readline().split()))
# 목표값 재조정
for i in range(target_count):
    current_target = targets[i]
    for j in range(i + 1, target_count):
        if current_target <= targets[j]:
            targets[j] -= 1
# 조정된 목표값을 바탕으로 최소 연산 수를 구한다.
result = 0
start_position = 1 # 처음은 1에서 출발한다.
for i2 in range(target_count):
    current_length = initial_queue_length - i2
    # 시작점에서 타겟까지 왼쪽으로 움직일 때의 거리를 구한다.
    left_moves = (targets[i2] - start_position) % current_length # % 연산은 start_position값이 target보다 커서 음수가 나올 경우, current_length를 더하는 효과를 낸다.
    # 오른쪽으로 움직이는 거리는 왼쪽으로 움직일 때의 거리 값을 이용해 간편하게 구한다.
    right_moves = current_length - left_moves
    result += min(left_moves, right_moves)
    start_position = targets[i2] # 추출 연산을 마친 후므로 시작점을 다시 구한다. 추출로 인한 위치 문제는 위 코드에서 사전에 처리했으므로 넘어가도 된다.
print(result)