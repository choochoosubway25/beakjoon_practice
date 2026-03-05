import time
import random
from collections import Counter


def test_function(problem_levels, player_levels, problem_count, user_count):
    if problem_count is None:
        problem_count = len(problem_levels)
    if user_count is None:
        user_count = len(player_levels)
    level_counts = Counter(problem_levels)
    solvable_list = [0 for _ in range(user_count)]
    max_level = max(problem_levels)
    level_list = [0 for _ in range(max_level + 1)]
    solvable = 0
    for i in range(1, max_level + 1):
        solvable += level_counts[i]
        level_list[i] = solvable
    for j in range(user_count):
        solvable_list[j] = level_list[player_levels[j]]
    maximum_limit = max(solvable_list)
    size_limit = 1
    while 3 * size_limit * (size_limit - 1) <= maximum_limit:
        size_limit += 1
    size_list = [3 * k * (k - 1) + 1 for k in range(size_limit+1)]
    size_list[0] = 0
    player_size = [0 for _ in range(user_count)]
    for i in range(user_count):
        for j in range(size_limit+1):
            if solvable_list[i] < size_list[j]:
                player_size[i] = j - 1
                break
    print(' '.join(map(str, player_size)))


if __name__ == '__main__':
    test_problem_count = 10
    test_player_count = 10
    test_problem_levels = [random.randint(1, 1000) for _ in range(test_problem_count)]
    test_player_levels = [random.randint(1, 1000) for _ in range(test_player_count)]
    start_time = time.process_time()
    test_function(test_problem_levels, test_player_levels, test_problem_count, test_player_count)
    end_time = time.process_time()
    print(end_time - start_time)