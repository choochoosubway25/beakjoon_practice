import random
alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
                 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'c=',
                 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in range(10):
    length = random.randint(2, 30)
    test_word = ''
    for j in range(length):
        test_word += random.choice(alphabet_list)
    print(test_word, length)