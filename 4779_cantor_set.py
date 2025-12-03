import sys


def cantor_set(size: int) -> str:
    if size == 0:
        return '-'
    else:
        sub_set = cantor_set(size-1)
        blank = ' ' * (3 ** (size-1))
        return sub_set+blank+sub_set


while True:
    try:
        size_num = int(sys.stdin.readline())
        print(cantor_set(size_num))
    except EOFError:
        break
    except ValueError:
        break
