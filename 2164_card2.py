import sys
import queue

card_list = queue.Queue()
number = int(sys.stdin.readline())
for _ in range(number):
    card_list.put(_+1)
while card_list.qsize() > 1:
    card_list.get()
    back_card = card_list.get()
    card_list.put(back_card)
print(card_list.get())
