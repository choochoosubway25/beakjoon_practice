import sys

'''
m : time limit
t : unit numbers
u : uphill time
f : flat ground time
d : downhill time
'''
m, t, u, f, d = map(int, sys.stdin.readline().split())
time_taken = [0 for _ in range(t)]
total_time = 0
for i in range(t):
    course = sys.stdin.readline().strip()
    if course == "u" or course == "d":
        total_time += u + d
        time_taken[i] = total_time
    else:
        total_time += 2 * f
        time_taken[i] = total_time
j = 0
for time in time_taken:
    if time <= m:
        j += 1
    else:
        break
print(j)
