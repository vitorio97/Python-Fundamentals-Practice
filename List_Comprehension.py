#New List with comprehension
print('\nNew List with Comprehension (ganjil) \n')
booklist = ['1 Tomato Plants', '2 Corn Plants', '3 Rice Field','4 Car Engines Lifespan','5 Apple Seed','6 Mango seed']
newbooklist = booklist[0::2] #start(index no.0 Tomato Plant):end:step
for i in range (0, len(newbooklist)):
    print(newbooklist[i])

#New List with comprehension
print('\nNew List with Comprehension (genap) \n')
booklist = ['1 Tomato Plants', '2 Corn Plants', '3 Rice Field','4 Car Engines Lifespan','5 Apple Seed','6 Mango seed']
newbooklist = booklist[1::2] #start:end:step
for i in range (0, len(newbooklist)):
    print(newbooklist[i])

#New List with comprehension
print('\nNew List with Comprehension (delete a numbers of element from behind) \n')
booklist = ['1 Tomato Plants', '2 Corn Plants', '3 Rice Field','4 Car Engines Lifespan','5 Apple Seed','6 Mango seed']
newbooklist = booklist[0:-2] #start:end
for i in range (0, len(newbooklist)):
    print(newbooklist[i])

#New List with comprehension
print('\nNew List with Comprehension (delete a numbers of element from behind and stepping) \n')
booklist = ['1 Tomato Plants', '2 Corn Plants', '3 Rice Field','4 Car Engines Lifespan','5 Apple Seed','6 Mango seed']
newbooklist = booklist[0:-2:2] #start:end:step
for i in range (0, len(newbooklist)):
    print(newbooklist[i])

#New List with comprehension
print('\nNew List with Comprehension \n')
booklist = ['1 Tomato Plants', '2 Corn Plants', '3 Rice Field','4 Car Engines Lifespan','5 Apple Seed','6 Mango seed']
print(booklist[0::2])
