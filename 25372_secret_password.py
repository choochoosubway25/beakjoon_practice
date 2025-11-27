import sys

num_iter = int(sys.stdin.readline())

for _ in range(num_iter):
    password = str(sys.stdin.readline().strip())
    result = "no"
    if 6 <= len(password) <= 9:
        result = "yes"
    print(result)
