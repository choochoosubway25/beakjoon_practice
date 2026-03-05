import sys
import re


string_count = int(sys.stdin.readline())
for _ in range(string_count):
    signals = sys.stdin.readline().strip()
    pattern = re.compile("(100+1+|01)+")
    if pattern.fullmatch(signals):
        print("YES")
    else:
        print("NO")