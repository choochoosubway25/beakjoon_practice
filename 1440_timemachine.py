import sys

time_str = str(sys.stdin.readline().strip())
time_digits = time_str.split(':')
hour_possibility = 0
impossibility = 1
for digit in time_digits:
    digit_int = int(digit)
    if 1 <= digit_int <= 12:
        hour_possibility += 1
    if digit_int > 59:
        impossibility = 0
print(hour_possibility * 2 * impossibility)
