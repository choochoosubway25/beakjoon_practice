a, b = map(str, input().split())
new_a = ''
new_b = ''
for i in range(len(a)-1, -1, -1):
    new_a += a[i]
for j in range(len(b)-1, -1, -1):
    new_b += b[j]
is_new_a_larger = int(new_a) > int(new_b)
if is_new_a_larger:
    print(new_a)
else:
    print(new_b)

