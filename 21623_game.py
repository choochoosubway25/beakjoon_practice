import sys

k, n = map(int, sys.stdin.readline().split())
scores = list(map(int, sys.stdin.readline().split()))
round_count = 0
current_score = n
for i in range(k):
    if current_score == 0:
        current_score = n
        round_count += 1
    given_score = scores[i]
    if current_score >= given_score:
        current_score -= given_score
if current_score == 0:
    round_count += 1
print(round_count)
print(current_score)
