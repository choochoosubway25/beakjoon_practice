import sys

test_count = int(sys.stdin.readline())
adding_list = [0, 1, 2, 4]
for _ in range(test_count):
    number = int(sys.stdin.readline())
    adding_list_index = len(adding_list)
    if number >= adding_list_index:
        for i in range(adding_list_index, number + 1):
            adding_list.append(adding_list[-1]+adding_list[-2]+adding_list[-3])
    print(adding_list[number])
