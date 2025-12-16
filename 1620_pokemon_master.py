import sys

dict_size, question_count = map(int, sys.stdin.readline().split())
pokemon_dict = dict()
for i in range(dict_size):
    pokemon_name = str(sys.stdin.readline().strip())
    indices = str(i+1)
    pokemon_dict[pokemon_name] = indices
    pokemon_dict[indices] = pokemon_name
for _ in range(question_count):
    question = str(sys.stdin.readline().strip())
    answer = pokemon_dict[question]
    print(answer)
