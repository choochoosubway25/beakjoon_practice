import sys

order_num = int(sys.stdin.readline())
count = 0
i = 665
while count < order_num:
    i += 1
    if '666' in str(i):
        count += 1
print(i)
