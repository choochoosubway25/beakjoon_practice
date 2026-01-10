import sys
from collections import Counter

word_length = int(sys.stdin.readline())
words = str(sys.stdin.readline().strip())
acid_counter = Counter(words)
result = acid_counter['A'] * acid_counter['C'] * acid_counter['G'] * acid_counter['T']
print(result % 1000000007)
