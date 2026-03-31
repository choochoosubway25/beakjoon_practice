import sys

a_value, b_value = 0, 0
for a in range(9):
    print(f"? A {a + 1}", flush=True)
    response = sys.stdin.readline().strip()
    if response == "1":
        a_value = a + 1
        break
for b in range(9):
    print(f"? B {b + 1}", flush=True)
    response = sys.stdin.readline().strip()
    if response == "1":
        b_value = b + 1
        break
print(f"! {a_value+b_value}", flush=True)
