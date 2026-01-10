import sys

votes_counts = list(map(int, sys.stdin.readline().split()))
sixteenth = votes_counts[0]
result = 0
for i in range(1, 5):
    votes = votes_counts[i]
    if sixteenth - votes <= 1000:
        result += 1
print(result)
