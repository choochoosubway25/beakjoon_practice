import sys

n, p = map(int, sys.stdin.readline().split())
days = list(map(int, sys.stdin.readline().split()))
answer = -1
start = 0
end = 1
while start < end <= n:
    streak = end - start + p
    distance = (days[end - 1] - days[start] + 1) - (end - start)
    if distance > p:
        start += 1
        if start == end:
            end += 1
    else:
        end += 1
        answer = max(answer, streak)
print(answer)
