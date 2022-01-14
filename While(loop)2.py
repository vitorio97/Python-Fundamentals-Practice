book=10
print("Teacher said, 'read all books'")
read_time=0

understood=0
print(f"No. book read and understood {understood}")

while read_time < book * 2:
    read_time = read_time + 1
    if understood == 9:
        print(f"Book no - {understood + 1 } not yet understood")
    else:
        understood = understood + 1
        print(f"Book No - {understood} has been read and understood")

print(f'Numbers of book already read {understood + 1}')


if understood == book:
    print("Task Done")
else:
    print(f"Not all books can be understood, only {understood}")