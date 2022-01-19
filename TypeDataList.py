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

print('\nChange Elements no.\n')
booklist = ['Tomato Plants', 'Corn Plants', 'Rice Field']
booklist[2] = 'How to Math for Basic'
for i in range (0, len(booklist)):
    print(booklist[i])

print('\nGet Element no 2 (from left to right)\n')
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

print('\ndel Command\n')
booklist = ['Tomato Plants', 'Corn Plants', 'Rice Field']
del booklist[0]
for i in range (0, len(booklist)):
    print(booklist[i])

print('\nList Comprehension Example\n')
booklist = ['Tomato Plants', 'Corn Plants', 'Rice Field']
del booklist[:]
#start:end
for i in range (0, len(booklist)):
    print(booklist[i])

print('\nList Comprehension Example\n')
booklist = ['Tomato Plants', 'Corn Plants', 'Rice Field']
del booklist[0:-1] #all elements deleted until elements no. -1 (from right)
for i in range (0, len(booklist)):
    print(booklist[i])

print('\nList Comprehension Step Example\n')
booklist = ['Tomato Plants', 'Corn Plants', 'Rice Field','Car Engines Lifespan','Lamb Meals for Kids','Apple Tree in Suburban']
del booklist[0::2] #Start:End:Step
for i in range (0, len(booklist)):
    print(booklist[i])