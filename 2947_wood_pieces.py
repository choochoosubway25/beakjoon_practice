import sys

wood_pieces = list(map(int, sys.stdin.readline().split()))
sort_finished = False
while not sort_finished:
    for i in range(len(wood_pieces) - 1):
        if wood_pieces[i] > wood_pieces[i + 1]:
            wood_pieces[i], wood_pieces[i + 1] = wood_pieces[i + 1], wood_pieces[i]
            print(' '.join(map(str, wood_pieces)))
    for i in range(len(wood_pieces)):
        if wood_pieces[i] != i + 1:
            break
    else:
        sort_finished = True
