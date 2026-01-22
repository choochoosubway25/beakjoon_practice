import sys

while True:
    input_str = str(sys.stdin.readline().strip())
    if input_str == '# 0 0':
        break
    inputs = input_str.split()
    name = inputs[0]
    age = int(inputs[1])
    weight = int(inputs[2])
    class_kind = 'Junior'
    if age > 17 or weight >= 80:
        class_kind = 'Senior'
    print(f'{name} {class_kind}')
