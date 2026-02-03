import sys

dice_1 = list(map(int, sys.stdin.readline().split()))
dice_2 = list(map(int, sys.stdin.readline().split()))
dice_3 = list(map(int, sys.stdin.readline().split()))
'''
dice_n_possibilities : [possibility for vs dice 1, possibility for vs dice 2, possibility for vs dice 3]
dice_winning_counts : 
[winning possibility for dice 1 vs dice 2, winning possibility for dice 1 vs dice 3, winning possibility for dice 2 vs dice 3]
'''
dice_1_possibilities = [0 for i1 in range(3)]
dice_2_possibilities = [0 for i2 in range(3)]
dice_3_possibilities = [0 for i3 in range(3)]
dice_winning_counts = [0 for ii in range(3)]
for i in range(6):
    for j in range(6):
        if dice_1[i] > dice_2[j]:
            dice_1_possibilities[1] += 1
            dice_winning_counts[0] += 1
        elif dice_1[i] < dice_2[j]:
            dice_2_possibilities[0] += 1
            dice_winning_counts[0] += 1
        if dice_1[i] > dice_3[j]:
            dice_1_possibilities[2] += 1
            dice_winning_counts[1] += 1
        elif dice_1[i] < dice_3[j]:
            dice_3_possibilities[0] += 1
            dice_winning_counts[1] += 1
        if dice_2[i] > dice_3[j]:
            dice_2_possibilities[2] += 1
            dice_winning_counts[2] += 1
        elif dice_2[i] < dice_3[j]:
            dice_3_possibilities[1] += 1
            dice_winning_counts[2] += 1
# count winning possibilities
is_dice_1_wins_dice_2 = (dice_1_possibilities[1] * 2 >= dice_winning_counts[0]) and dice_winning_counts[0] > 0
is_dice_2_wins_dice_1 = (dice_2_possibilities[0] * 2 >= dice_winning_counts[0]) and dice_winning_counts[0] > 0
is_dice_1_wins_dice_3 = (dice_1_possibilities[2] * 2 >= dice_winning_counts[1]) and dice_winning_counts[1] > 0
is_dice_3_wins_dice_1 = (dice_3_possibilities[0] * 2 >= dice_winning_counts[1]) and dice_winning_counts[1] > 0
is_dice_2_wins_dice_3 = (dice_2_possibilities[2] * 2 >= dice_winning_counts[2]) and dice_winning_counts[2] > 0
is_dice_3_wins_dice_2 = (dice_3_possibilities[1] * 2 >= dice_winning_counts[2]) and dice_winning_counts[2] > 0
result = None
if is_dice_3_wins_dice_1 and is_dice_3_wins_dice_2:
    result = "3"
if is_dice_2_wins_dice_1 and is_dice_2_wins_dice_3:
    result = "2"
if is_dice_1_wins_dice_2 and is_dice_1_wins_dice_3:
    result = "1"
if result is None:
    result = "No dice"
print(result)
