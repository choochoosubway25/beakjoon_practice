import sys

rows, columns, people = map(int, sys.stdin.readline().split())
result = 0
for i in range(rows):
    column = sys.stdin.readline().strip()
    start, end = 0, people
    is_vacancy = False
    while end < columns:
        if not is_vacancy:
            sub_str = column[start:end]
            if '1' in sub_str:
                start += 1
                end += 1
            else:
                is_vacancy = True
                result += 1
        else:
            if end + 1 < columns and column[end + 1] == "0":
                result += 1
                end += 1
            else:
                is_vacancy = False
                end += people
print(result)
