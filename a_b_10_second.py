import sys
import random

a_value, b_value = 0, 0
a_set = set()
b_set = set()

k = 10000
for _ in range(k - 1):
    if _ == 0:
        i = 1
    elif _ == 1:
        i = k
    else:
        i = random.randint(2, k - 1)
        while i in a_set:
            i = random.randint(2, k - 1)
    print(f"? A {i}", flush=True)
    response = int(sys.stdin.readline())
    if response == 1:
        a_value = i
        a_remains = k - _
        break
    else:
        a_set.add(i)
else:
    remains = set(range(2, k + 1)) - set(a_set)
    a_value = list(remains)[0]
    a_remains = 0
limit = min([k - 2 + a_remains, k - 1])
for _ in range(limit):
    if _ == 0:
        i = 1
    elif _ == 1:
        i = k
    else:
        i = random.randint(2, k - 1)
        while i in b_set:
            i = random.randint(2, k - 1)
    print(f"? B {i}", flush=True)
    response = int(sys.stdin.readline())
    if response == 1:
        b_value = i
        break
    else:
        b_set.add(i)
else:
    remains = set(range(2, k + 1)) - set(b_set)
    b_value = list(remains)[0]
    b_remains = 0

print(f"! {a_value + b_value}", flush=True)