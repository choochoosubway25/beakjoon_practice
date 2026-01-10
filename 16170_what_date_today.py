from datetime import date
today = str(date.today())
for word in today.split('-'):
    print(word)
