import sys

'''
수열 'x_n: 출발할 때 부터 n번째 정류장을 지난 다음의 승객 수'라 정의하자. 
한 정류장을 지날 때 지나기 전과 지난 후의 승객의 수는 다음과 같다.
x_n = x_(n-1)/2 - 1/2
이를 다시 풀어 쓰면, x_(n-1) = 2*x_n + 1
이를 이용해서 수열 'y_n: 마지막 정류장에서 n개 정류장을 지나기 직전 승객 수'라 정의하면
다음과 같이 쓸 수 있다.
y_n = 2 * y_(n-1) + 1, y_0 = 0
이를 다음과 같이 정리하면 다음과 같다.
(y_n + 1) = 2 * (y_(n-1) + 1)
따라서 수열 'z_n = y_n + 1' 이라 정리하면 z_n은 다음과 같다.
z_n = 2 * z_(n-1), z_1 = 1
이 경우 일반항은 z_n = 2^n (n >= 0)으로 표현 가능하다.
이를 이용하면 y_n의 값을 다음과 같이 구할 수 있다.
y_n = 2^n - 1
'''
test_count = int(sys.stdin.readline())
for _ in range(test_count):
    stop_num = int(sys.stdin.readline())
    print(2 ** stop_num - 1)
