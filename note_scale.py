note_list = map(int, input().split())
note_list = list(note_list)

result = ""
diff = 0
diff = note_list[1] - note_list[0]
for i in range(1, len(note_list)-1):
    if diff != note_list[i+1] - note_list[i]:
        result = "mixed"
        break
else:
    if diff > 0:
        result = "ascending"
    else:
        result = "descending"

print(result)