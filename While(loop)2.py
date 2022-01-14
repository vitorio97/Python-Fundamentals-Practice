book_sum=10
print("Teacher said, 'read all books'")
total_read=0

book_read_understood=0
print(f"No. book read and understood {book_read_understood}")

while total_read < book_sum * 2:
    total_read = total_read + 1
    if book_read_understood == 9:
        print(f"Book no - {book_read_understood +1 } not yet understood")
    else:
        book_read_understood = book_read_understood + 1
        print(f"Book No - {book_read_understood} has been read and understood")

print(f'Numbers of book already read {book_read_understood}')


if book_read_understood == book_sum:
    print("Task Done")
else:
    print(f"Not all books can be understood, only {book_read_understood}")