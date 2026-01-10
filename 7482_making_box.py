import sys

'''
박스의 크기 V는 다음과 같다.
V = (a-2b)*(a-2b)*b
박스식을 b에 대해 미분하면
V' = (a-2b)(a-6b)
이 때 V'가 0이 되는 경우는 a=2b 또는 a=6b
그런데 a=2b인 경우에는 V의 값이 0이 되므로 제외된다.
따라서 a=6b일 때 박스의 값이 최대가 된다. 따라서 b = a/6
'''
test_count = int(sys.stdin.readline())
for _ in range(test_count):
    a = float(sys.stdin.readline())
    print(f'{a/6:0.10f}')
