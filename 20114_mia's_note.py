import sys

string_length, height_length, width_length = map(int, sys.stdin.readline().split())
restored_string = ["?" for _ in range(string_length)]
restoring_string = list(sys.stdin.readline().strip())
for i in range(1, height_length):
    blurred_string = sys.stdin.readline().strip()
    for j in range(width_length*string_length):
        if blurred_string[j] != "?":
            restoring_string[j] = blurred_string[j]
for k in range(string_length):
    restore_block = restoring_string[k*width_length:(k+1)*width_length]
    chars = set(restore_block)
    for char in chars:
        if char != "?":
            restored_string[k] = char
print("".join(restored_string))
