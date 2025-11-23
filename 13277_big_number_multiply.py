a, b = map(int, input().split())

result = str()
if a == 0 or b == 0:
    result = '0'
else:
    div_size = max((len(f'{a}'), len(f'{b}'))) // 2 + max((len(f'{a}'), len(f'{b}'))) % 2
    sub_mul = 0
    a_front = str(a)[:-div_size]
    if a_front == '':
        a_front = '0'
    a_back = str(a)[-div_size:]
    b_front = str(b)[:-div_size]
    if b_front == '':
        b_front = '0'
    b_back = str(b)[-div_size:]
    sub_mul = int(a_back) * int(b_back)
    remains = sub_mul // 10**div_size
    result = str(sub_mul)[-div_size:]
    sub_mul = int(a_front) * int(b_back) + int(b_front) * int(a_back) + remains
    remains = sub_mul // 10**div_size
    if sub_mul != 0:
        result = str(sub_mul)[-div_size:] + result
    sub_mul = int(a_front) * int(b_front) + remains
    if sub_mul != 0:
        result = str(sub_mul) + result
print(result)
