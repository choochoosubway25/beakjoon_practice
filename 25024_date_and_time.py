def is_time_readable(x: int, y: int) -> str:
    result = "No"
    if 0 <= x <= 23 and 0 <= y <= 59:
        result = "Yes"
    return result


def is_date_readable(x: int, y: int) -> str:
    result = "No"
    date_dict = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    if x in date_dict.keys():
        if 1 <= y <= date_dict[x]:
            result = "Yes"
    return result


n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    print(f'{is_time_readable(x, y)} {is_date_readable(x, y)}')

