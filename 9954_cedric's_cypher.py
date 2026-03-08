import sys


def cypher(character, shifting_num):
    result = character
    if 65 <= ord(character) <= 96:
        new_num = (ord(character) - 65 - shifting_num) % 26
        result = chr(new_num + 65)
    elif 97 <=  ord(character) <= 122:
        new_num = (ord(character) - 97 - shifting_num) % 26
        result = chr(new_num + 97)
    return result



while True:
    strings = sys.stdin.readline().strip()
    if strings == "#":
        break
    shift_key = strings[-1]
    main_massage = strings[:-1]
    shift_number = ord(shift_key) - ord('A')
    shift_list = [shift_number] * len(main_massage)
    new_massage = map(cypher, main_massage, shift_list)
    print(''.join(new_massage))
