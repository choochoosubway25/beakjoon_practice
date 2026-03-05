import sys
from collections import Counter

holes_dict = {'A':1, 'B':2, 'D':1, 'O':1, 'P':1, 'Q':1, 'R':1}
test_count = int(sys.stdin.readline())
for _ in range(test_count):
    new_sentence = sys.stdin.readline().strip()
    alphabet_counts = Counter(new_sentence)
    result = 0
    for key in holes_dict.keys():
        result += alphabet_counts[key] * holes_dict[key]
    print(result)
