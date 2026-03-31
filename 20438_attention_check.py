import sys
from bisect import bisect_left, bisect_right


student_count, snoozing_count, query_count, interval_count = map(int, sys.stdin.readline().split())
snoozing_students = set(map(int, sys.stdin.readline().split()))
query_students = set(map(int, sys.stdin.readline().split()))
student_set = set([n+3 for n in range(student_count)])
student_set -= snoozing_students
for query_student in query_students:
    if query_student in snoozing_students:
        continue
    check_set = set(range(query_student, student_count + 3, query_student))
    student_set -= check_set
absence_list = list(student_set | snoozing_students)
absence_list.sort()
for _ in range(interval_count):
    start, end = map(int, sys.stdin.readline().split())
    start_index = bisect_left(absence_list, start)
    end_index = bisect_right(absence_list, end)
    print(end_index - start_index)
