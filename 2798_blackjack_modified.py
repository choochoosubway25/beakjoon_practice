def find_max_sum(cards: list[int], targets: int) -> int:
    list_length = len(cards)
    max_value = 0
    for i in range(list_length):
        for j in range(i+1, list_length):
            for k in range(j+1, list_length):
                sums = cards[i] + cards[j] + cards[k]
                if max_value < sums <= targets:
                    max_value = sums
    return max_value


card_num, target = map(int, input().split())
card_list = list(map(int, input().split()))
card_list.sort()
print(find_max_sum(card_list, target))
