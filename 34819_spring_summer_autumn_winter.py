import sys


month_count, query_count = map(int, sys.stdin.readline().split())
contests_counts = list(map(int, sys.stdin.readline().split()), int)
season_list = ['Winter', 'Spring', 'Summer', 'Autumn']
season_index = 1
season_dict = dict()
prepared = False
for _ in range(query_count):
    query = sys.stdin.readline().split()
    month_index = int(query[1])
    if query[0] == '1':
        contests_counts[month_index] = int(query[2])
        prepared = False
    else:
        if not prepared:
            season_index = 1
            season_dict[1] = season_list[season_index]
            for i in range(2, month_count + 1):
                contest_delta = contests_counts[i] - contests_counts[i - 1]
                if contest_delta < 0:
                    season_index = 0
                elif contest_delta > 0:
                    season_index = 2
                else:
                    season_index = 2 * (season_index // 2) + 1
                season_dict[i] = season_list[season_index]
            prepared = True
        print(season_dict[month_index])
