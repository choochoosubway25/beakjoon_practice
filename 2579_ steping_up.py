import sys

step_count = int(sys.stdin.readline())
step_score = list()
step_maximum = [-1 for _ in range(step_count)]
for _ in range(step_count):
    score = int(sys.stdin.readline())
    step_score.append(score)
step_maximum[0] = step_score[0]
if step_count > 1:
    step_maximum[1] = step_score[0] + step_score[1]
if step_count > 2:
    step_maximum[2] = max(step_score[0], step_score[1]) + step_score[2]
for i in range(3, step_count):
    before_one_step = step_score[i-1] + step_maximum[i-3]
    before_two_step = step_maximum[i-2]
    step_maximum[i] = max(before_two_step, before_one_step) + step_score[i]
print(step_maximum[-1])
