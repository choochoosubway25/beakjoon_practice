import sys


while True:
    round_count = int(sys.stdin.readline())
    if round_count == 0:
        break
    mark_turns = sys.stdin.readline().split()
    leti_turns = sys.stdin.readline().split()
    mark_sum = sum(map(int, mark_turns))
    leti_sum = sum(map(int, leti_turns))
    mark_streak_count, leti_streak_count = 0, 0
    mark_before_score, leti_before_score = "", ""
    for i in range(round_count):
        mark_score = mark_turns[i]
        leti_score = leti_turns[i]
        if mark_before_score == mark_score:
            mark_streak_count += 1
        else:
            mark_streak_count = 1
            mark_before_score = mark_score
        if leti_before_score == leti_score:
            leti_streak_count += 1
        else:
            leti_streak_count = 1
            leti_before_score = leti_score
        if mark_streak_count == 3 or leti_streak_count == 3:
            if leti_streak_count != 3:
                mark_sum += 30
            if mark_streak_count != 3:
                leti_sum += 30
            break
    if mark_sum > leti_sum:
        print("M")
    elif mark_sum < leti_sum:
        print("L")
    else:
        print("T")
