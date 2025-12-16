import sys

a_total, b_total = map(int, sys.stdin.readline().split())
# 과녁의 점수는 binary로 표현 가능하며, c의 점수는 a,b의 비트의 xor 값이다.
print(a_total ^ b_total)
