"""
WBWBWB

WBWBWB -> 0
BWBWBW -> 6
"""

# count missmatch with starting of white
def count_missmatch(blocks: str):
    miss_match_count: int = 0
    for color in blocks[0::2]:
        if color != 'W':
            miss_match_count += 1
    for color in blocks[1::2]:
        if color != 'B':
            miss_match_count += 1
    return miss_match_count



rows, columns = map(int, input().split())
board = list()
minimum_missmatch = -1
for i in range(rows):
    word = str(input())
    board.append(word)
for i in range(columns - 8):
    misscount_white = list()
    misscount_black = list()
    for word in board:
        sub_word = word[i:i+8]
        white_misscount = count_missmatch(sub_word)
        misscount_white.append(white_misscount)
        misscount_black.append(8 - white_misscount)
    print(misscount_white)
    print(misscount_black)
    print('---------------')



