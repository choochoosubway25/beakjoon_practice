participations_num = int(input())
shirt_order_nums = list(map(int, input().split()))
shirt_bundle, pen_bundle = map(int, input().split())
shirt_order = 0
for order_num in shirt_order_nums:
    shirt_order += order_num // shirt_bundle
    if order_num % shirt_bundle != 0:
        shirt_order += 1
print(shirt_order)
print(f'{participations_num//pen_bundle} {participations_num%pen_bundle}')
