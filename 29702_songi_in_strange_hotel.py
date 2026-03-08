import sys

"""
문제풀이
여기서 주어진 순서를 2진수로 전환하면 다음과 같다.
01XXXXXX 
여기서 앞의 0을 모두 제거한 문자열의 길이는 층수, 앞의 1을 제외한 부분 : 호실 - 1 의 이진법 변환
이를 이용해 2진수 변환 뒤에 오른쪽 비트 쉬프팅을 진행하면, 위로 올라가는 방의 번호가 된다.
이를 포맷에 맞춰서 출력하면 된다.
"""

test_count = int(sys.stdin.readline())
for _ in range(test_count):
    numbers = int(sys.stdin.readline())
    bin_convert = bin(numbers)[2:]
    floor_number = len(bin_convert)
    room_number = numbers - 2 ** (floor_number - 1)
    while numbers > 0:
        print(f"{floor_number}{room_number+1:0>18}")
        numbers = (numbers >> 1)
        floor_number -= 1
        room_number = (room_number >> 1)
