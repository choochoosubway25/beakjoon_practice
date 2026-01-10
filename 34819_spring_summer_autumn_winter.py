import sys


month_count, query_count = map(int, sys.stdin.readline().split())
contests_data = map(int, sys.stdin.readline().split())
contests_counts = [0 for _ in range(month_count)]
i = 0
for count in contests_data:
    contests_counts[i] = count
    i += 1
season_list = ['Winter', 'Spring', 'Summer', 'Autumn']
season_index = 1
season_record = ['' for _ in range(month_count)]
season_record[0] = 'Spring'
updated_indices = 1
for _ in range(query_count):
    query = sys.stdin.readline().split()
    month_index = int(query[1]) - 1
    if query[0] == '1':
        contests_counts[month_index] = int(query[2])
        updated_indices = 1
    else:
        season_index = 1
        for j in range(updated_indices, month_index + 1):
            contest_delta = contests_counts[j] - contests_counts[j - 1]
            if contest_delta > 0:
                season_index = 2
            elif contest_delta < 0:
                season_index = 0
            else:
                season_index = 2 * (season_index // 2) + 1
            season_record[j] = season_list[season_index]
            updated_indices = month_index
        print(season_record[month_index])
