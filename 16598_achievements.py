import sys

n, p = map(int, sys.stdin.readline().split())
days = list(map(int, sys.stdin.readline().split()))
distances = [days[i + 1] - days[i] - 1 for i in range(len(days) - 1)]
start = 0
end = 0
answer_start = -1
answer_end = -1
sub_sum = 0
remains = -1
max_find = False
while start <= end < n-1:
    if sub_sum < p:
        if not max_find:
            answer_start = start
            answer_end = end
            remains = p - sub_sum
        sub_sum += distances[end]
        end += 1
    elif sub_sum > p:
        sub_sum -= distances[start]
        start += 1
    else:
        max_find = True
        answer_start = start
        answer_end = end
        end += 1
if max_find:
    print(days[answer_end] - days[answer_start] + 1)
else:
    print(days[answer_end] - days[answer_start] + 1 + remains)
