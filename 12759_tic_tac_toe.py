import sys


def is_win(positions: set) -> bool:
    win_set = [{1, 2, 3}, {4, 5, 6}, {7, 8, 9}, {1, 4, 7}, {2, 5, 8}, {3, 6, 9}, {1, 5, 9}, {3, 5, 7}]
    for set_case in win_set:
        if set_case <= positions:
            return True
    return False

player_1_positions = set()
player_2_positions = set()
current_player = int(sys.stdin.readline())
result = 0
for _ in range(9):
    inputs = sys.stdin.readline().strip()
    if inputs == "":
        break
    x, y = map(int, inputs.split())
    position = (x - 1) * 3 + y
    if current_player == 1:
        player_1_positions.add(position)
        if is_win(player_1_positions):
            result = 1
            break
        current_player = 2
    else:
        player_2_positions.add(position)
        if is_win(player_2_positions):
            result = 2
            break
        current_player = 1
print(result)
