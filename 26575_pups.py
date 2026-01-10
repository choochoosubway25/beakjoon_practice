import sys

case_count = int(sys.stdin.readline())
for _ in range(case_count):
    dogs, food_per_dog, food_per_pound = map(float, sys.stdin.readline().split())
    result = dogs * food_per_dog * food_per_pound
    result = int((100 * result) + 0.5) / 100
    print(f'${result:0.2f}')
