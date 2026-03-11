import sys
from unittest import case

test_count = int(sys.stdin.readline())
for _ in range(test_count):
    book_count = int(sys.stdin.readline())
    books = list(map(int, sys.stdin.readline().split()))
    alex_books = list()
    bob_books = list()
    alex_indices = set()
    bob_indices = set()
    for i in range(book_count):
        book_worth = books[i]
        if book_worth % 2 == 0:
            bob_books.append(book_worth)
            bob_indices.add(i)
        else:
            alex_books.append(book_worth)
            alex_indices.add(i)
    alex_books.sort()
    bob_books.sort()
    bob_books.reverse()
    new_books = [0 for k in range(book_count)]
    for i in range(book_count):
        if i in alex_indices:
            new_books[i] = alex_books.pop(0)
        else:
            new_books[i] = bob_books.pop(0)
    sorted_books = " ".join(map(str, new_books))
    print(f"Case #{_ + 1}: {sorted_books}")