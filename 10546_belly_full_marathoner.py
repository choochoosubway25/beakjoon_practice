import sys
from collections import Counter

runner_count = int(sys.stdin.readline())
runner_list = ['' for _ in range(runner_count)]
for _ in range(runner_count):
    runner = str(sys.stdin.readline().strip())
    runner_list[_] = runner
runners = Counter(runner_list)
finished_list = ['' for _ in range(runner_count - 1)]
for _ in range(runner_count - 1):
    runner = str(sys.stdin.readline().strip())
    finished_list[_] = runner
finishers = Counter(finished_list)
runners.subtract(finishers)
print(runners.most_common(1)[0][0])
