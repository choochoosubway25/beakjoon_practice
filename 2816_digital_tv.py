import sys

channel_count = int(sys.stdin.readline())
channel_list = ['' for i in range(channel_count)]
kbs1_index = -1
kbs2_index = -1
button_order = str()
for _ in range(channel_count):
    channel_name = str(sys.stdin.readline().strip())
    channel_list[_] = channel_name
    if channel_name == "KBS1":
        kbs1_index = _
    if channel_name == "KBS2":
        kbs2_index = _
button_order = button_order + kbs1_index * '1' + kbs1_index * '4'
if kbs1_index > kbs2_index:
    kbs2_index += 1
button_order = button_order + kbs2_index * '1' + (kbs2_index - 1) * '4'
print(button_order)
