import sys

string_count = int(sys.stdin.readline())
magnet_string = str(sys.stdin.readline().strip())
one_char_lengths = list()
length = 1
for i in range(string_count-1):
    if magnet_string[i+1] != magnet_string[i]:
        one_char_lengths.append(length)
        length = 1
    else:
        length += 1
one_char_lengths.append(length)
if len(one_char_lengths) > 1:
    max_length = 0
    for j in range(len(one_char_lengths)-1):
        magnet_length = min(one_char_lengths[j+1], one_char_lengths[j])
        magnet_length *= 2
        if magnet_length > max_length:
            max_length = magnet_length
    print(max_length)
else:
    print(0)
