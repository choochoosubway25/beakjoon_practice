import sys
from collections import Counter


four_hour_counter = Counter()
six_hour_counter = Counter()
ten_hour_counter = Counter()
result = "Yes"
workers_set = set()
week_count = int(sys.stdin.readline())
for _ in range(week_count):
    morning_schedules = sys.stdin.readline().split()
    four_hour_counter.update(morning_schedules)
    midtime_schedules = sys.stdin.readline().split()
    six_hour_counter.update(midtime_schedules)
    evening_schedules = sys.stdin.readline().split()
    four_hour_counter.update(evening_schedules)
    night_schedules = sys.stdin.readline().split()
    ten_hour_counter.update(night_schedules)
workers_set = workers_set | set(four_hour_counter.keys())
workers_set = workers_set | set(six_hour_counter.keys())
workers_set = workers_set | set(ten_hour_counter.keys())
workers_times = Counter()
for worker in workers_set:
    if worker == "-":
        continue
    workers_times[worker] += 4 * four_hour_counter[worker]
    workers_times[worker] += 6 *six_hour_counter[worker]
    workers_times[worker] += 10 * ten_hour_counter[worker]
if len(workers_times) > 0:
    if max(workers_times.values()) > min(workers_times.values()) + 12:
        result = "No"
print(result)
