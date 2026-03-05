import sys


press_count = int(sys.stdin.readline())
result = 0
is_running = False
start_time = 0
for _ in range(press_count):
    press_time = int(sys.stdin.readline())
    if is_running:
        result += press_time - start_time
    else:
        start_time = press_time
    is_running = not is_running
if is_running:
    print("still running")
else:
    print(result)
