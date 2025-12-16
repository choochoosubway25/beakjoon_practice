import sys

song_count, fade_time = map(int, sys.stdin.readline().split())
total_time = 0
for i in range(song_count):
    minute, second = map(int, sys.stdin.readline().split(':'))
    if i > 0:
        total_time -= fade_time
    total_time += minute * 60 + second
total_hour, total_min, total_second = \
    total_time // 3600, (total_time % 3600) // 60, total_time % 60
print(f'{total_hour:02}:{total_min:02}:{total_second:02}')
