booklist = ['Tomato Plants', 'Corn Plants', 'Rice Field']
print('Shows Booklist Variables')
print(booklist)

print('\nProcessing All with for in')
for book in booklist:
    print(book)

print('\nShows Book in Index no - ')
print(booklist[0])
print(booklist[1])
print(booklist[2])

print('\nShows Book with in range')
for i in range (0, len(booklist)):
    print(booklist[i])

booklist = [1, 'Watermelon Plants', -314, 3.14]

print('\nShows Book with in range where as Datatype are Differents')
for i in range (0, len(booklist)):
    print(booklist[i])

print('\nReturning Start Value')
booklist = ['Tomato Plants', 'Corn Plants', 'Rice Field']
print('\nAdding one new book')
booklist.append('Farming Rice')

for i in range (0, len(booklist)):
    print(booklist[i])

print('\nClear List')
booklist.clear()
for i in range (0, len(booklist)):
    print(booklist[i])

print('\nChange Elements\n')
booklist = ['Tomato Plants', 'Corn Plants', 'Rice Field']
booklist[2] = 'How to Math for Basic'
for i in range (0, len(booklist)):
    print(booklist[i])

print('\nGet Element no 2\n')
book = booklist.pop(1)
for i in range (0, len(booklist)):
    print(booklist[i])

print('\nTaken Book\n')
print(book)

print('\nPop\n')
booklist.pop()
for i in range (0, len(booklist)):
    print(booklist[i])

print('\nPop -1 (which is Rice Field)\n')
booklist = ['Tomato Plants', 'Corn Plants', 'Rice Field']
booklist.pop(-1)
for i in range (0, len(booklist)):
    print(booklist[i])