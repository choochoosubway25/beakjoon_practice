import sys

num_iter = int(sys.stdin.readline())
for _ in range(num_iter):
    inputs = sys.stdin.readline().split()
    times = int(inputs[0])
    chars = str(inputs[1])
    result = chars * times
    print(result)
