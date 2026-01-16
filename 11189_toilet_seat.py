import sys

character = str(sys.stdin.readline().strip())
initial_count = 0
if character[0] != character[1]:
    initial_count += 1
policy_1_count = initial_count
policy_2_count = initial_count
policy_3_count = initial_count
if character[1] == 'D':
    policy_1_count += 1
else:
    policy_2_count += 1
for i in range(2, len(character)):
    if character[i] == 'D':
        policy_1_count += 2
    else:
        policy_2_count += 2
    if character[i] != character[i-1]:
        policy_3_count += 1
print(policy_1_count)
print(policy_2_count)
print(policy_3_count)
