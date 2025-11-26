import heapq
import sys

word_set = set()
word_heap = list()

iter_num = int(sys.stdin.readline())

for _ in range(iter_num):
    word = str(sys.stdin.readline())
    word_set.add(word)

for word in word_set:
    heapq.heappush(word_heap, (len(word), word))

while len(word_heap) > 0:
    word_sort = heapq.heappop(word_heap)
    print(word_sort[1].strip())
