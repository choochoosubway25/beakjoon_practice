import sys

problem_count, tester_count = map(int, sys.stdin.readline().split())
score_list = list(map(int, sys.stdin.readline().split()))
maximum_score = -1
maximum_student = -1
for _ in range(tester_count):
    exam_result = list(sys.stdin.readline().split())
    student_num = int(exam_result[0])
    total_score = 0
    for i in range(problem_count):
        is_right = (exam_result[i+1]=='O')
        if is_right:
            total_score += score_list[i]
    if total_score > maximum_score:
        maximum_score = total_score
        maximum_student = student_num
    elif total_score == maximum_score and student_num < maximum_student:
        maximum_student = student_num
print(f'{maximum_student} {maximum_score}')
