import sys

case_count = int(sys.stdin.readline())
result = 0
for _ in range(case_count):
    d_day = str(sys.stdin.readline())
    date = int(d_day[2:])
    if date <= 90:
        result += 1
print(result)
