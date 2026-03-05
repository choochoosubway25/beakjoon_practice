import sys

states = sys.stdin.readline().strip()
# 주어진 문자를 역전시켜 2진수 활용이 쉽도록 함
lengths = len(states)
states = states[::-1]
# 주어진 문자를 0, 1로 변환한 뒤에 2진수로 변환하도록 함
states = states.replace("Y", "1")
states = states.replace("N", "0")
binary_states = int('0b' + states, 2)
result = 0
i = 0
# 전구가 모두 꺼져있다면, binary_states는 0이 됨.
while binary_states > 0:
    # flip을 할 부분을 찾는다. (i+1)의 배수 번째 만큼 1로 표시하도록 한다.
    flip_string = '0b' + ('1' + ('0' * i)) * (lengths // (i + 1))
    flip_binary = int(flip_string, 2)
    # (i+1)번째 비트가 1이라면 flip을 하고 결과값에 1을 더한다.
    if (1 << i) & binary_states != 0:
        result += 1
        binary_states = binary_states ^ (((2 << lengths) - 1) & flip_binary)
    i += 1
print(result)
