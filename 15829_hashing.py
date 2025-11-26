def alphabet_to_number(alphabet: str) -> int:
    return ord(alphabet) - 96


def hashing(sentence: str, length: int = -1, r: int = 31, p: int = 1234567891) -> int:
    if length < 0:
        length = len(sentence)
    result = 0
    cof_num = 1
    for i in range(length):
        hash_value = (alphabet_to_number(sentence[i]) * cof_num) % p
        result = (result + hash_value) % p
        cof_num = (cof_num * r) % p
    return result


word_length = int(input())
word = str(input())
print(hashing(word, word_length))
