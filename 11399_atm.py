import sys

people_count = int(sys.stdin.readline())
time_counts = list(map(int, sys.stdin.readline().split()))
time_taken = 0
time_total = 0
for _ in range(people_count):
    min_time = min(time_counts)
    time_taken += min_time
    time_total += time_taken
    time_counts.remove(min_time)
print(time_total)
